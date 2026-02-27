import html
import os

from PySide6.QtCore import Signal, Qt
from PySide6.QtGui import QMouseEvent
from PySide6.QtWidgets import (
    QFrame, QVBoxLayout, QGroupBox
)

from PDFSearchService import PDFSearchService
from flow_layout import FlowLayout
from pdf_occurrence import PDFOccurrence
from ui.ui_search_card import Ui_search_card
from ui.ui_search_list_item import Ui_search_list_item
from ui.ui_search_screen import Ui_GroupBox


class OccurrenceCard(QFrame):
    double_click_signal = Signal()

    def __init__(self, occurrence: PDFOccurrence, parent=None):
        super().__init__(parent)
        self.ui = Ui_search_card()
        self.ui.setupUi(self)

        highlighted_text = self.highlight_match(
            occurrence.context,
            occurrence.start_position,
            occurrence.end_position
        )

        self.ui.occurrence_page_number.setText(f"📄 Страница №{occurrence.page_number}")
        self.ui.occurrence_text.setText(highlighted_text)

    def highlight_match(self, context, start_pos: int, end_pos: int):
        before = html.escape(context[:start_pos])
        highlighted = html.escape(context[start_pos:end_pos])
        after = html.escape(context[end_pos:])

        # Формируем HTML
        html_result = f"""
                <html>
                    <body style="color: white; font-size: 9pt;">
                        {before}<span style="background-color: yellow; color: black;">{highlighted}</span>{after}
                    </body>
                </html>
                """

        return html_result

    def mouseDoubleClickEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            self.double_click_signal.emit()


class SearchListItem(QFrame):

    def __init__(self, filename: str, occurrences: list, parent=None):
        super().__init__(parent)
        self.ui = Ui_search_list_item()
        self.ui.setupUi(self)

        self.ui.file_name.setText(self._format_filename(filename))
        self.ui.occurrence_counter.setText(f"Найдено вхождений - {len(occurrences)}")

        # Создаем FlowLayout для карточек
        self.cards_flow_grid = FlowLayout(self.ui.search_cards, spacing=10)
        self.ui.search_cards.setLayout(self.cards_flow_grid)

        self.cards = []

    def add_occurrence(self, occurrence: PDFOccurrence):
        card = OccurrenceCard(occurrence)
        self.cards.append(card)
        self.cards_flow_grid.addWidget(card)

    def _format_filename(self, filename: str) -> str:
        if len(filename) <= 30:
            return filename

        name, ext = os.path.splitext(filename)
        if len(name) > 30:
            name = name[:27] + "..."

        return f"{name}{ext}"


class SearchScreen(QGroupBox):
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

        self.search_list_layout = QVBoxLayout()
        self.search_list_layout.setContentsMargins(0, 0, 0, 0)
        self.search_list_layout.setSpacing(10)
        self.ui.search_list.setLayout(self.search_list_layout)

        # Хранилище для результатов
        self.search_results = {}  # filename -> [(page_num, text), ...]

    def set_file_paths(self, file_paths: list[str]):
        self.file_paths = file_paths

    def perform_search(self):
        """Выполняет поиск по всем PDF"""
        query = self.ui.search_field.toPlainText().strip()
        if not query:
            return

        # Очищаем предыдущие результаты
        self.clear_results()

        # Выполняем поиск
        for pdf_path in self.file_paths:
            occurrences = PDFSearchService.search_with_context(pdf_path, query, 250)
            if occurrences:
                filename = os.path.basename(pdf_path)
                self.search_results[filename] = occurrences

                # Создаем элемент списка
                item = SearchListItem(filename, occurrences)

                for occurrence in occurrences:
                    item.add_occurrence(occurrence)

                self.search_list_layout.addWidget(item)

    def clear_results(self):
        """Очищает результаты поиска"""
        # Удаляем все виджеты кроме stretch
        while self.search_list_layout.count() > 1:
            item = self.search_list_layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

        self.search_results.clear()

    def clear_search(self):
        """Очищает поле поиска и результаты"""
        self.ui.search_field.clear()
        self.clear_results()