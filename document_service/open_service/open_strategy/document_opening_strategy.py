from abc import ABC, abstractmethod

from document_service.document import Document


class DocumentOpenStrategy(ABC):

    @abstractmethod
    def open_document(self, doc: Document):
        pass


class DocumentHighlightedOpenStrategy(DocumentOpenStrategy):

    def __init__(self, query: str, page: int):
        self.query = query
        self.page = page

    @abstractmethod
    def open_document(self, doc: Document):
        pass