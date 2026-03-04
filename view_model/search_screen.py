import html
import os

from PySide6.QtCore import Signal, Qt, QThread
from PySide6.QtGui import QMouseEvent
from PySide6.QtWidgets import (
    QFrame, QVBoxLayout, QGroupBox
)

from document_service.document import Document
from document_service.opening_service.document_opening_service import DocumentOpeningService
from document_service.parsing_service.doc_fragment import DocElementMetadataType
from document_service.search_service.doc_search_service import DocumentSearchService
from document_service.search_service.search_match import SearchMatch
from flow_layout import FlowLayout
from ui.ui_search_card import Ui_search_card
from ui.ui_search_list_item import Ui_search_list_item
from ui.ui_search_screen import Ui_GroupBox
from view_model.search_progress_data import SearchProgress


class MatchCard(QFrame):
    double_click_signal = Signal(object)

    def __init__(self, match: SearchMatch, parent=None):
        super().__init__(parent)
        self.ui = Ui_search_card()
        self.ui.setupUi(self)
        self.match = match

        highlighted_text = self.highlight_match(
            match.matched_text,
            match.context.context_before,
            match.context.context_after
        )

        self.ui.occurrence_page_number.setText(f"📄 Страница №{match.element_metadata.get(DocElementMetadataType.PAGE_NUMBER)}")
        self.ui.occurrence_text.setText(highlighted_text)

    def highlight_match(self, match: str, context_before: str, context_after: str):
        before = html.escape(context_before)
        highlighted = html.escape(match)
        after = html.escape(context_after)

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
            self.double_click_signal.emit(self.match)


class SearchListItem(QFrame):

    def __init__(self, filename: str, occurrences: list, parent=None):
        super().__init__(parent)
        self.ui = Ui_search_list_item()
        self.ui.setupUi(self)

        self.ui.file_name.setText(self._format_filename(filename))
        self.ui.occurrence_counter.setText(f"Найдено вхождений: {len(occurrences)}")

        # Создаем FlowLayout для карточек
        self.cards_flow_grid = FlowLayout(self.ui.search_cards, spacing=10)
        self.ui.search_cards.setLayout(self.cards_flow_grid)

    def add_match(self, match_card: MatchCard):
        self.cards_flow_grid.addWidget(match_card)

    def _format_filename(self, filename: str) -> str:
        if len(filename) <= 30:
            return filename

        name, ext = os.path.splitext(filename)
        if len(name) > 30:
            name = name[:27] + "..."

        return f"{name}{ext}"


class SearchWorker(QThread):
    query: str
    documents: list[Document]

    file_search_started = Signal(object)
    file_search_finished = Signal(object, list)
    fragment_search_finished = Signal(float)
    match_found = Signal()

    def __init__(self):
        super().__init__()
        self.search_service = DocumentSearchService(
            self.fragment_search_finished_callback,
            self.match_found_callback
        )
        self._is_running = True

    def run(self):
        self._is_running = True
        for doc in self.documents:
            if not self._is_running:
                break

            self.file_search_started.emit(doc)

            search_matches: list[SearchMatch] = self.search_service.search(
                query=self.query,
                file_path=doc.file_path,
                file_type=doc.file_type,
                context_length=250,
                max_workers=os.cpu_count()
            )

            if self._is_running:
                self.file_search_finished.emit(doc, search_matches)
                self.msleep(max(50, len(search_matches) * 10))

    def set_query(self, query: str):
        self.query = query

    def set_documents(self, documents: list[Document]):
        self.documents = documents

    def fragment_search_finished_callback(self, progress: float):
        self.fragment_search_finished.emit(progress)

    def match_found_callback(self):
        self.match_found.emit()

    def stop(self):
        self._is_running = False


class SearchScreen(QGroupBox):
    back_clicked = Signal()

    def __init__(self, documents: list[Document]=None, parent=None):
        super().__init__(parent)
        self.ui = Ui_GroupBox()
        self.ui.setupUi(self)

        if documents is None: self.documents = []
        else: self.documents = documents

        # Устанавливаем layout для списка
        self.search_list_layout = QVBoxLayout()
        self.search_list_layout.setContentsMargins(0, 0, 0, 0)
        self.search_list_layout.setSpacing(10)
        self.ui.search_list.setLayout(self.search_list_layout)

        # Поиск
        self.is_searching = False
        self.search_results: dict[Document, list[SearchMatch]] = {}
        self.matches_count = 0
        self.search_progress = SearchProgress()
        self.searcher = SearchWorker()

        # Устанавливаем действия для кнопок
        self.setup_connections()

        # Создаем экземпляр сервиса для открытия файлов
        self.doc_open_service = DocumentOpeningService()

    def setup_connections(self):
        # Настраиваем взаимодействие с кнопкой "назад"
        self.ui.return_button.clicked.connect(self.on_back_button_pressed)

        # Настраиваем взаимодействие с полем поиска и соответствующими кнопками
        self.ui.search_field.textChanged.connect(self.on_search_field_text_changed)
        self.ui.search_field.returnPressed.connect(self.start_searching)
        self.ui.search_button.clicked.connect(self.start_searching)
        self.ui.clear_search_button.clicked.connect(self.clear_search)

        # Назначаем колбэки поисковика
        self.searcher.file_search_started.connect(self.file_search_started)
        self.searcher.file_search_finished.connect(self.file_search_finished)
        self.searcher.fragment_search_finished.connect(self.fragment_search_finished)
        self.searcher.match_found.connect(self.match_found_callback)

    def set_file_paths(self, documents: list[Document]):
        self.documents = documents

    def start_searching(self):
        query = self.ui.search_field.text().strip()
        if not query:
            return

        # Очищаем предыдущие результаты
        self.clear_results()

        self.is_searching = True

        # Устанавливаем видимость и заполняем необходимые поля
        self.search_progress.set_files_count(len(self.documents))
        self.ui.progress_text.setText(self.search_progress.to_string())
        self.ui.matches_text.setText(f"Найдено вхождений: {self.matches_count}")

        # Начинаем поиск в дополнительном потоке
        self.searcher.set_query(query)
        self.searcher.set_documents(self.documents)
        self.searcher.start()

    def on_back_button_pressed(self):
        self.clear_search()
        self.back_clicked.emit()

    def on_search_field_text_changed(self, text):
        has_text = bool(text and text.strip())
        self.ui.clear_search_button.setEnabled(has_text)

    def on_match_card_double_clicked(self, match: SearchMatch):
        file_path = match.file_path
        page = match.element_metadata.get(DocElementMetadataType.PAGE_NUMBER)
        self.doc_open_service.open_file(file_path)

    def file_search_started(self, doc: Document):
        if self.is_searching:
            self.search_progress.set_current_file(doc.file_name)
            self.search_progress.increment_file_num()
            self.ui.progress_text.setText(self.search_progress.to_string())

    def file_search_finished(self, doc: Document, search_matches: list[SearchMatch]):
        if self.is_searching:
            if search_matches:
                # Создаем элемент списка и добавляем все карточки вхождений
                file_list_item = SearchListItem(doc.file_name, search_matches)
                for match in search_matches:
                    card = MatchCard(match)
                    card.double_click_signal.connect(self.on_match_card_double_clicked)
                    file_list_item.add_match(card)

                self.search_list_layout.addWidget(file_list_item)
                self.search_results[doc] = search_matches

            if self.search_progress.current_file_num == len(self.documents):
                self.is_searching = False

    def fragment_search_finished(self, progress: float):
        pass

    def match_found_callback(self):
        if self.is_searching:
            self.matches_count += 1
            self.ui.matches_text.setText(f"Найдено вхождений: {self.matches_count}")

    def stop_searching(self):
        self.is_searching = False
        self.searcher.stop()

    def clear_results(self):
        self.stop_searching()

        self.ui.progress_text.setText("")
        self.ui.matches_text.setText("")

        while self.search_list_layout.count() > 0:
            item = self.search_list_layout.takeAt(0)
            item.widget().deleteLater()

        self.search_progress.clear_progress()
        self.search_results.clear()
        self.matches_count = 0


    def clear_search(self):
        self.ui.search_field.clear()
        self.clear_results()