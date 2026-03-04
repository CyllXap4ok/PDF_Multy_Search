import re
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Callable

from document_service.parsing_service.doc_fragment import DocumentFragment
from document_service.document import FileType
from document_service.parsing_service.doc_to_fragments_parser import DocumentParser
from document_service.parsing_service.strategy.strategies_dict import PARSING_STRATEGIES
from document_service.search_service.search_match import MatchContext, SearchMatch


class DocumentSearchService:

    def __init__(
            self,
            fragment_search_finished: Callable[[float], None],
            match_found: Callable[[], None],
    ):
        self.fragment_search_finished = fragment_search_finished
        self.match_found = match_found
        self.parser = DocumentParser()
        self._is_cancelled = False

    def search(
            self,
            query: str,
            file_path: str,
            file_type: FileType,
            context_length: int,
            max_workers: int = 1
    ) -> list[SearchMatch]:
        """
        Ищет вхождение строки в документе. Перед началом поиска документ разбивается на фрагменты
        :param query: Строковой запрос для поиска в документе
        :param file_path: Путь к файлу, в котором необходимо выполнить поиск
        :param file_type: Тип файла
        :param context_length: Длина контекста, окружающего найденное вхождение
        :param max_workers: количество потоков для выполнения поиска по фрагментам. Значение по-умолчанию = 1
        :return Список вхождений, найденных в документе
        :raises Exception: в случае, если query - пустая строка
        """

        query_length = len(query)
        if query_length == 0: raise ValueError("Query is empty")

        self.parser.set_strategy(PARSING_STRATEGIES.get(file_type))
        fragments: list[DocumentFragment] = self.parser.parse_file(file_path)
        fragments_size = len(fragments)

        shifts: dict[str, int] = {
            query[i]: max(1, query_length - i - 1)
            for i in range(query_length)
        }

        matches: list[SearchMatch] = []
        matches_lock = threading.Lock()

        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            future_to_index = {}

            for i, fragment in enumerate(fragments):
                if self._is_cancelled:
                    executor.shutdown(wait=False)
                    return []

                future = executor.submit(
                    self.__search_in_fragment__,
                    query,
                    query_length,
                    context_length,
                    fragment,
                    file_path,
                    file_type,
                    shifts
                )

                future_to_index[future] = i

            for future in as_completed(future_to_index):
                if self._is_cancelled:
                    return []

                fragment_matches = future.result()
                if fragment_matches:
                    with matches_lock:
                        progress: float = i / fragments_size
                        self.fragment_search_finished(progress)
                        matches.extend(fragment_matches)

        return matches

    def __search_in_fragment__(
            self,
            query: str,
            query_length: int,
            context_length: int,
            fragment: DocumentFragment,
            file_path: str,
            file_type: FileType,
            shifts: dict[str, int] = None
    ) -> list[SearchMatch]:
        matches: list[SearchMatch] = []

        if not shifts:
            shifts: dict[str, int] = {
                query[i]: max(1, query_length - i - 1)
                for i in range(query_length)
            }

        for element in fragment.elements:
            element_content = element.content

            try:
                indexes = self.boyer_moore_search(query, element_content, shifts)

                for index in indexes:
                    context = self.__get_context__(element_content, index, query_length, context_length)

                    match = SearchMatch(
                        query,
                        context,
                        index,
                        element.element_type,
                        element.metadata,
                        file_path,
                        file_type
                    )

                    matches.append(match)

            except ValueError:
                pass

        return matches

    def boyer_moore_search(
            self,
            pattern: str,
            text: str,
            shifts: dict[str, int] = None
    ) -> list[int]:

        indexes: list[int] = []
        text_length = len(text)
        pattern_length = len(pattern)

        if pattern_length > text_length:
            raise ValueError("Pattern length is greater than text length")

        if shifts is None:
            shifts = {
                pattern[i]: max(1, pattern_length - i - 1)
                for i in range(pattern_length)
            }

        current_position = 0

        while current_position + pattern_length < text_length:
            comparison_index = pattern_length - 1

            while comparison_index >= 0 and pattern[comparison_index].lower() == text[current_position + comparison_index].lower():
                comparison_index -= 1

            if comparison_index < 0:
                indexes.append(current_position)
                current_position += pattern_length - 1
                self.match_found()
            else:
                mismatched_char = text[current_position + comparison_index].lower()
                shift = shifts.get(mismatched_char, pattern_length)
                current_position += shift

        return indexes

    def __get_context__(
            self,
            text: str,
            match_start_position: int,
            match_length: int,
            context_length: int
    ) -> MatchContext:
        text_length = len(text)
        match_end_position = match_start_position + match_length

        # Вычисляем доступную длину контекста с каждой стороны
        available_before = match_start_position
        available_after = text_length - match_end_position

        # Распределяем контекст поровну, но не больше доступного
        half_context = max(0, (context_length - match_length) // 2)

        context_before_length = min(half_context, available_before)
        context_after_length = min(half_context, available_after)

        # Если осталось место, распределяем его
        remaining = context_length - (match_length + context_before_length + context_after_length)
        if remaining > 0:
            # Сначала добавляем к after, если есть место
            add_to_after = min(remaining, available_after - context_after_length)
            context_after_length += add_to_after
            remaining -= add_to_after

            # Затем к before, если осталось
            if remaining > 0:
                context_before_length += min(remaining, available_before - context_before_length)

        # Извлекаем контекст
        context_before = text[match_start_position - context_before_length:match_start_position]
        context_after = text[match_end_position:match_end_position + context_after_length]

        context_before = self.__clean_text__(context_before).lstrip()
        context_after = self.__clean_text__(context_after).rstrip()

        return MatchContext(
            context_before=context_before,
            context_after=context_after
        )

    @staticmethod
    def __clean_text__(text: str) -> str:

        # Заменяем множественные пробелы на один
        text = re.sub(r'\s+', ' ', text)
        # Заменяем множественные абзацы на один
        text = re.sub(r'\n\s*\n', '\n', text)
        # Заменяем множественные точки на троеточие
        text = re.sub(r'\.{4,}', '...', text)

        return text