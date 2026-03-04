from abc import ABC, abstractmethod

from document_service.parsing_service.doc_fragment import DocumentFragment


class ParsingStrategy(ABC):

    @abstractmethod
    def parse_file(self, file_path) -> list[DocumentFragment]:
        pass
