from PySide6.QtCore import QUrl
from PySide6.QtGui import QDesktopServices

from document_service.document import Document
from document_service.open_service.open_strategy.default_strategy import DefaultDocumentOpenStrategy
from document_service.open_service.open_strategy.document_opening_strategy import DocumentOpenStrategy


class DocumentOpeningService:
    def __init__(self, opening_strategy: DocumentOpenStrategy = DefaultDocumentOpenStrategy):
        self.opening_strategy = opening_strategy

    def set_strategy(self, opening_strategy: DocumentOpenStrategy):
        self.opening_strategy = opening_strategy

    def open_document(self, doc: Document):
        self.opening_strategy.open_document(doc)