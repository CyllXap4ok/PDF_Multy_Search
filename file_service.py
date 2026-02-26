from PySide6.QtCore import QUrl
from PySide6.QtGui import QDesktopServices


class QFileService:
    def __init__(self):
        pass

    @staticmethod
    def open_file(file_path: str):
        QDesktopServices.openUrl(QUrl.fromLocalFile(file_path))