import html

from PySide6.QtCore import Signal, Qt, QThread
from PySide6.QtGui import QMouseEvent
from PySide6.QtWidgets import (
    QFrame, QVBoxLayout, QGroupBox, QWidget
)

from document_service.document import Document
from document_service.open_service.document_opening_service import DocumentOpeningService
from document_service.open_service.open_strategy.pdf_open_strategy import PdfHighlightedOpenStrategy
from document_service.search_service.search_match import SearchMatch
from document_service.search_service.search_process_manager import DocumentSearchProcessManager
from flow_layout import FlowLayout
from search_progress_data import SearchProgress
from ui.ui_search_card import Ui_search_card
from ui.ui_search_file_item import Ui_search_file_item
from ui.ui_search_screen import Ui_GroupBox


class MatchCard(QFrame):
    double_click_signal = Signal(object)

    def __init__(self, match: SearchMatch, parent=None):
        super().__init__(parent)
        self.ui = Ui_search_card()
        self.ui.setupUi(self)
        self.match = match

        highlighted_text = self.highlight_match(
            match.query,
            match.context.before,
            match.context.after
        )

        self.ui.occurrence_page_number.setText(f"📄 Страница №{match.document_page}")
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


class SearchFileItem(QWidget):

    matches = 0

    def __init__(self, document: Document, parent=None):
        super().__init__(parent)
        self.ui = Ui_search_file_item()
        self.ui.setupUi(self)

        self.ui.file_name = document.file_name
        self.ui.file_type = document.document_type.extension

    def set_search_status(self, new_status: str):
        self.ui.search_status.setText(new_status)

    def increase_match_count(self):
        self.matches += 1
        self.ui.match_count.setText(str(self.matches))

    def set_match_count(self, new_count: int):
        self.ui.match_count.setText(str(new_count))


class SearchWorker(QThread):
    query: str
    documents: list[Document]

    document_search_started = Signal(object)
    document_search_finished = Signal(object, list)
    document_search_progress = Signal(object, float)
    matches_found = Signal(object, list)

    def __init__(self, search_process_manager: DocumentSearchProcessManager):
        super().__init__()
        search_process_manager.set_document_search_started_callback(self.document_search_started_callback)
        search_process_manager.set_document_search_finished_callback(self.document_search_finished_callback)
        search_process_manager.set_document_search_progress_callback(self.document_search_progress_callback)
        search_process_manager.set_matches_found_callback(self.matches_found_callback)

        self.search_process_manager = search_process_manager
        self.processed_files_counter = 0
        self._is_searching = False

    def run(self):
        self._is_searching = True
        self.processed_files_counter = 0
        self.search_process_manager.submit_tasks(self.query, self.documents)

        while self._is_searching:
            self.search_process_manager.handle_pending_results(0.1)

    def document_search_started_callback(self, document: Document):
        self.document_search_started.emit(document)

    def document_search_finished_callback(self, document: Document, matches: list[SearchMatch]):
        self.processed_files_counter += 1
        if self.processed_files_counter == len(self.documents): self._is_searching = False
        self.document_search_finished.emit(document, matches)

    def document_search_progress_callback(self, document: Document, progress: int):
        self.document_search_progress.emit(document, progress)

    def matches_found_callback(self, document: Document, matches: list[SearchMatch]):
        self.matches_found.emit(document, matches)

    def stop_searching(self):
        self._is_searching = False
        self.search_process_manager.stop_searching()

    def set_query(self, query: str):
        self.query = query

    def set_documents(self, documents: list[Document]):
        self.documents = documents


class SearchScreen(QGroupBox):
    back_clicked = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_GroupBox()
        self.ui.setupUi(self)

        self.documents = []

        self.scroll_widget = QWidget()
        self.documents_list_layout = QVBoxLayout(self.scroll_widget)
        self.documents_list_layout.setContentsMargins(0, 0, 0, 0)
        self.documents_list_layout.setSpacing(0)
        self.ui.documents_scroll_area.setWidget(self.scroll_widget)

        self.matches_scroll_container = QWidget()
        self.matches_grid = FlowLayout(self.matches_scroll_container)
        self.ui.search_results_scroll_area.setWidget(self.matches_scroll_container)

        # Поиск
        self.search_results: dict[Document, list[SearchMatch]] = {}
        self.matches_count = 0
        search_process_manager = DocumentSearchProcessManager() # Создаем менеджер процессов поиска
        search_process_manager.start_process_pool() # Запускаем фоновые процессы поиска, ожидающие задачи
        self.searcher = SearchWorker(search_process_manager) # Передаем менеджер процессов исполнителю
        self.search_progress = SearchProgress()

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
        self.searcher.document_search_started.connect(self.document_search_started)
        self.searcher.document_search_finished.connect(self.document_search_finished)
        self.searcher.document_search_progress.connect(self.document_search_progress)
        self.searcher.matches_found.connect(self.matches_found)

    def start_searching(self):
        query = self.ui.search_field.text().strip()
        if not query:
            return

        # Очищаем предыдущие результаты
        self.clear_results()

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
        query = match.query
        page = match.document_page
        document = match.from_document
        self.doc_open_service.set_strategy(PdfHighlightedOpenStrategy(query, page))
        self.doc_open_service.open_document(document)

    def document_search_started(self, document: Document):
        self.search_progress.increment_file_num()
        self.ui.progress_text.setText(self.search_progress.to_string())

    def document_search_finished(self, doc: Document, search_matches: list[SearchMatch]):
        if search_matches:
            # Создаем элемент списка и добавляем все карточки вхождений
            file_list_item = SearchListItem(doc.file_name, search_matches)
            for match in search_matches:
                card = MatchCard(match)
                card.double_click_signal.connect(self.on_match_card_double_clicked)
                file_list_item.add_match(card)

            self.search_list_layout.addWidget(file_list_item)
            self.search_results[doc] = search_matches

    def document_search_progress(self, document: Document, progress: float):
        pass

    def matches_found(self, document: Document, matches: list[SearchMatch]):
        self.matches_count += len(matches)
        self.ui.matches_text.setText(f"Найдено вхождений: {self.matches_count}")

    def stop_searching(self):
        self.searcher.stop_searching()

    def set_documents(self, documents: list[Document]):
        self.documents = documents
        for doc in documents:
            self.documents_list_layout.addWidget(SearchFileItem(doc))


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