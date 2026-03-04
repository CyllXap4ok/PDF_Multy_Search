from abc import ABC, abstractmethod

from document_service.document import Document


class OpeningStrategy(ABC):

    @abstractmethod
    def open_document(self, doc: Document):
        pass