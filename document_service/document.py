from pathlib import Path
from enum import Enum


class FileType(Enum):
    PDF = ("PDF", ".pdf")
    DOCX = ("DOCX", ".docx")
    TXT = ("TXT", ".txt")

    def __init__(self, name, extension):
        self._name = name
        self.extension = extension

    @classmethod
    def from_extension(cls, extension: str) -> 'FileType':
        """Определяет FileType по расширению файла"""
        for file_type in cls:
            if file_type.extension == extension.lower():
                return file_type
        raise ValueError(f"Unsupported file extension: {extension}")


class Document:

    def __init__(self, file_path: str):
        path = Path(file_path)

        self.file_name = path.name
        self.file_path = file_path
        self.file_type = FileType.from_extension(path.suffix)