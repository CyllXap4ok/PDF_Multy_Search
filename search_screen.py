import os

import pymupdf
from PySide6.QtCore import Signal, Qt
from PySide6.QtWidgets import (
    QFrame, QWidget, QVBoxLayout
)

from flow_layout import FlowLayout
from ui.ui_search_card import Ui_search_card
from ui.ui_search_list_item import Ui_search_list_item
from ui.ui_search_screen import Ui_GroupBox


class SearchCard(QFrame):

    def __init__(self, page_num: int, text: str, search_query: str, parent=None):
        super().__init__(parent)
        self.ui = Ui_search_card()
        self.ui.setupUi(self)

        # Устанавливаем номер страницы
        self.ui.occurrence_page_number.setText(f"📄 Страница №{page_num}")

        # Форматируем текст с выделением совпадения
        formatted_text = self._format_search_text(text, search_query)
        self.ui.occurrence_text.setText(formatted_text)
        self.ui.occurrence_text.setTextFormat(Qt.TextFormat.RichText)

    def _format_search_text(self, text: str, query: str) -> str:
        """Выделяет совпадение желтым цветом"""
        # Экранируем специальные символы для HTML
        text = text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
        query_escaped = query.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')

        # Находим все вхождения запроса (регистронезависимо)
        import re
        pattern = re.compile(re.escape(query_escaped), re.IGNORECASE)

        # Заменяем каждое вхождение на выделенное желтым
        formatted = pattern.sub(
            lambda m: f'<span style="background-color: yellow; color: black;">{m.group(0)}</span>',
            text
        )

        return formatted


class SearchListItem(QWidget):
    """Элемент списка для одного файла со всеми вхождениями"""

    def __init__(self, filename: str, occurrences: list, search_query: str, parent=None):
        super().__init__(parent)
        self.ui = Ui_search_list_item()
        self.ui.setupUi(self)

        # Устанавливаем имя файла (обрезаем если длинное)
        self.ui.file_name.setText(self._format_filename(filename))

        # Устанавливаем счетчик вхождений
        self.ui.occurrence_counter.setText(f"Найдено вхождений - {len(occurrences)}")

        # Создаем FlowLayout для карточек
        self.flow_layout = FlowLayout(self.ui.search_item_header, margin=0, spacing=5)
        self.ui.search_item_header.setLayout(self.flow_layout)

        # Настраиваем кнопку скрытия/показа результатов
        self.results_visible = True
        self.ui.hide_results_button.clicked.connect(self.toggle_results)

        # Добавляем карточки вхождений
        self.cards = []
        for page_num, text in occurrences:
            card = SearchCard(page_num, text, search_query)
            self.cards.append(card)
            self.flow_layout.addWidget(card)

    def _format_filename(self, filename: str) -> str:
        """Обрезает длинное имя файла"""
        if len(filename) <= 30:
            return filename

        name, ext = os.path.splitext(filename)
        if len(name) > 27:
            name = name[:24] + "..."

        return f"{name}{ext}"

    def toggle_results(self):
        """Скрывает или показывает результаты поиска"""
        self.results_visible = not self.results_visible

        for card in self.cards:
            card.setVisible(self.results_visible)

        # Меняем стрелку
        if self.results_visible:
            self.ui.hide_results_button.setText("▼")
        else:
            self.ui.hide_results_button.setText("▶")


class SearchScreen(QWidget):
    back_clicked = Signal()

    def __init__(self, file_paths: list[str]=None, parent=None):
        super().__init__(parent)
        self.ui = Ui_GroupBox()
        self.ui.setupUi(self)

        if file_paths is None:
            self.file_paths = []
        else:
            self.file_paths = file_paths

        # Настраиваем поиск
        self.ui.search_button.clicked.connect(self.perform_search)
        self.ui.clear_search_button.clicked.connect(self.clear_search)
        self.ui.return_button.clicked.connect(self.back_clicked.emit)

        # Подключаем поиск по Enter
        self.ui.plainTextEdit.textChanged.connect(self.on_text_changed)

        # Создаем layout для списка результатов
        self.results_layout = QVBoxLayout(self.ui.search_list)
        self.results_layout.setSpacing(10)
        self.results_layout.setContentsMargins(5, 5, 5, 5)
        self.results_layout.addStretch()

        # Хранилище для результатов
        self.search_results = {}  # filename -> [(page_num, text), ...]

    def set_file_paths(self, file_paths: list[str]):
        self.file_paths = file_paths

    def on_text_changed(self):
        """Обработчик изменения текста поиска"""
        # Можно добавить автоматический поиск при вводе
        pass

    def perform_search(self):
        """Выполняет поиск по всем PDF"""
        query = self.ui.plainTextEdit.toPlainText().strip()
        if not query:
            return

        # Очищаем предыдущие результаты
        self.clear_results()

        # Выполняем поиск
        for pdf_path in self.file_paths:
            occurrences = self.search_in_pdf(pdf_path, query)
            if occurrences:
                filename = os.path.basename(pdf_path)
                self.search_results[filename] = occurrences

                # Создаем элемент списка
                item = SearchListItem(filename, occurrences, query)
                self.results_layout.insertWidget(self.results_layout.count() - 1, item)

    def search_in_pdf(self, pdf_path: str, query: str) -> list:
        """Ищет запрос в PDF и возвращает список (номер_страницы, текст)"""
        occurrences = []

        try:
            doc = pymupdf.open(pdf_path)

            for page_num in range(len(doc)):
                page = doc[page_num]
                text = page.get_text()

                # Ищем все вхождения (регистронезависимо)
                import re
                pattern = re.compile(re.escape(query), re.IGNORECASE)

                for match in pattern.finditer(text):
                    start, end = match.span()

                    # Получаем контекст 250 символов
                    context = self._get_context(text, start, end)
                    occurrences.append((page_num + 1, context))

            doc.close()
        except Exception as e:
            print(f"Ошибка при открытии {pdf_path}: {e}")

        return occurrences

    def _get_context(self, text: str, match_start: int, match_end: int) -> str:
        """Возвращает контекст длиной 250 символов с выделенным совпадением"""
        # Определяем границы контекста
        context_length = 250
        half_context = (context_length - (match_end - match_start)) // 2

        start = max(0, match_start - half_context)
        end = min(len(text), match_end + half_context)

        # Если не хватает символов, расширяем в другую сторону
        if end - start < context_length:
            if start == 0:
                end = min(len(text), start + context_length)
            else:
                start = max(0, end - context_length)

        context = text[start:end]

        # Очищаем текст от лишних пробелов и многоточий
        context = self._clean_text(context)

        return context

    def _clean_text(self, text: str) -> str:
        """Очищает текст от лишних пробелов, абзацев и многоточий"""
        # Заменяем множественные пробелы на один
        import re
        text = re.sub(r'\s+', ' ', text)

        # Заменяем абзацы и переносы строк на пробелы
        text = text.replace('\n', ' ').replace('\r', ' ').replace('\t', ' ')

        # Заменяем многоточия (4+ точек) на троеточие
        text = re.sub(r'\.{4,}', '...', text)

        # Убираем лишние пробелы в начале и конце
        text = text.strip()

        return text

    def clear_results(self):
        """Очищает результаты поиска"""
        # Удаляем все виджеты кроме stretch
        while self.results_layout.count() > 1:
            item = self.results_layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

        self.search_results.clear()

    def clear_search(self):
        """Очищает поле поиска и результаты"""
        self.ui.plainTextEdit.clear()
        self.clear_results()