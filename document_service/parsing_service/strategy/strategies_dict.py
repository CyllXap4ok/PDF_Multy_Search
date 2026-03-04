from typing import Dict

from document_service.document import FileType
from document_service.parsing_service.strategy.parsing_strategy import ParsingStrategy
from document_service.parsing_service.strategy.pdf_parsing_strategy import PDFParsingStrategy

PARSING_STRATEGIES: Dict[FileType, ParsingStrategy] = {
    FileType.PDF: PDFParsingStrategy()
}
