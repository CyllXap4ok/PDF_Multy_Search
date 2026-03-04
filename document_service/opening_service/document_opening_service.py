from PySide6.QtCore import QUrl
from PySide6.QtGui import QDesktopServices

from document_service.document import Document
from document_service.opening_service.opening_strategy.default_strategy import DefaultOpeningStrategy
from document_service.opening_service.opening_strategy.document_opening_strategy import OpeningStrategy


class DocumentOpeningService:
    def __init__(self, opening_strategy: OpeningStrategy = DefaultOpeningStrategy):
        self.opening_strategy = opening_strategy

    def set_strategy(self, opening_strategy: OpeningStrategy):
        self.opening_strategy = opening_strategy

    def open_document(self, doc: Document):
        self.opening_strategy.open_document(doc)

    @staticmethod
    def open_file(file_path: str):
        QDesktopServices.openUrl(QUrl.fromLocalFile(file_path))