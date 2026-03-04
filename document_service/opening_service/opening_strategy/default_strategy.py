from PySide6.QtCore import QUrl
from PySide6.QtGui import QDesktopServices

from document_service.document import Document
from document_service.opening_service.opening_strategy.document_opening_strategy import OpeningStrategy


class DefaultOpeningStrategy(OpeningStrategy):
    def open_document(self, doc: Document):
        QDesktopServices.openUrl(QUrl.fromLocalFile(doc.file_path))