import re
from abc import ABC, abstractmethod
from typing import Callable

from document_service.document import Document
from document_service.search_service.search_match import MatchContext, SearchMatch


class SearchStrategy(ABC):

    @abstractmethod
    def search(
            self,
            query: str,
            document: Document,
            context_length: int,
            progress_update: Callable[[float], None],
            matches_found: Callable[[list[SearchMatch]], None]
    ) -> list[SearchMatch]:
        pass

    @staticmethod
    def __boyer_moore_search__(pattern: str, text: str, shifts: dict[str, int] = None) -> list[int]:
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
            before=context_before,
            after=context_after
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