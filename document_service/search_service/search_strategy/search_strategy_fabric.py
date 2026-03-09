from document_service.document import Document, DocumentType
from document_service.search_service.search_strategy.docx_search_strategy import DocxSearchStrategy
from document_service.search_service.search_strategy.pdf_search_strategy import PdfSearchStrategy
from document_service.search_service.search_strategy.search_strategy import SearchStrategy


class SearchStrategyFabric:

    @staticmethod
    def create(document: Document) -> SearchStrategy:
        match document.document_type:
            case DocumentType.PDF:
                return PdfSearchStrategy()
            case DocumentType.DOCX:
                return DocxSearchStrategy()
            case DocumentType.TXT:
                pass

        raise RuntimeError(f'Document type {document.document_type} not supported')