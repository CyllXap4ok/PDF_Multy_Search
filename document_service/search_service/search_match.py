from dataclasses import dataclass
from typing import Dict, Any

from document_service.parsing_service.doc_fragment import DocElementMetadataType, ElementType
from document_service.document import FileType


@dataclass
class MatchContext:
    context_before: str
    context_after: str


@dataclass
class SearchMatch:
    matched_text: str
    context: MatchContext

    position_within_element: int
    from_element: ElementType
    element_metadata: Dict[DocElementMetadataType, Any]

    file_path: str
    file_type: FileType