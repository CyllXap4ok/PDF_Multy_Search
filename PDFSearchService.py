import pymupdf
import re

from pdf_occurrence import PDFOccurrence


class PDFSearchService:

    @staticmethod
    def search_with_context(file_path: str, query: str, context_length: int) -> list[PDFOccurrence]:
        occurrences = []

        try:
            doc = pymupdf.open(file_path)

            for page_num in range(len(doc)):
                page = doc[page_num]
                text = page.get_text()

                #Создаём паттерн для поиска
                pattern = re.compile(re.escape(query), re.IGNORECASE)

                for match in pattern.finditer(text):
                    start, end = match.span()

                    # Получаем контекст с заданным количеством символов
                    context = PDFSearchService.__get_context__(text, start, end, context_length)

                    occurrence = PDFOccurrence(context, start, end, page_num+1)
                    occurrences.append(occurrence)

            doc.close()
        except Exception as e:
            print(f"Ошибка при открытии {file_path}: {e}")

        return occurrences

    @staticmethod
    def __get_context__(
            text: str,
            occurrence_start_position: int,
            occurrence_end_position: int,
            context_length: int
    ) -> str:

        half_context = (context_length - (occurrence_end_position - occurrence_start_position)) // 2

        start = max(0, occurrence_start_position - half_context)
        end = min(len(text), occurrence_end_position + half_context)

        # Если не хватает символов, расширяем в другую сторону
        if end - start < context_length:
            if start == 0:
                end = min(len(text), start + context_length)
            else:
                start = max(0, end - context_length)

        context = text[start:end]

        # Очищаем текст от лишних пробелов и многоточий
        context = PDFSearchService.__clean_text__(context)

        return context

    @staticmethod
    def __clean_text__(text: str) -> str:

        # Заменяем множественные пробелы на один
        text = re.sub(r'\s+', ' ', text)
        # Заменяем множественные абзацы на один
        text = re.sub(r'\n\s*\n', '\n', text)
        # Заменяем множественные точки на троеточие
        text = re.sub(r'\.{4,}', '...', text)
        # Убираем лишние пробелы в начале и конце
        text = text.strip()

        return text