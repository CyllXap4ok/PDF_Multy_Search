from enum import Enum
from pathlib import Path


class DocumentType(Enum):
    PDF = ("PDF", ".pdf")
    DOCX = ("DOCX", ".docx")
    TXT = ("TXT", ".txt")

    def __init__(self, name, extension):
        self._name = name
        self.extension = extension

    @classmethod
    def from_extension(cls, extension: str) -> 'DocumentType':
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
        self.document_type = DocumentType.from_extension(path.suffix)

    def __eq__(self, other):
        name_eq = self.file_name == other.file_name
        path_eq = self.file_path == other.file_path
        type_eq = self.document_type == other.document_type
        return name_eq and path_eq and type_eq
