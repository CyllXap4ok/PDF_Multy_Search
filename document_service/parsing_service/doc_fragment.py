from dataclasses import dataclass, field
from enum import Enum
from typing import Dict, Any

from document_service.document import FileType


class ElementType(Enum):
    PARAGRAPH = "paragraph"
    IMAGE = "image"
    TABLE_CELL = "table_cell"


class DocElementMetadataType(Enum):
    PAGE_NUMBER = "page_number"
    TABLE_INDEX = "table_index"
    TABLE_ROW = "table_row"
    TABLE_COLUMN = "table_column"
    CELL_INDEX = "cell_index"
    IMAGE_INDEX = "image_index"


@dataclass
class DocumentElement:
    content: str
    element_type: ElementType
    metadata: Dict[DocElementMetadataType, Any] = None


@dataclass
class DocumentFragment:
    file_path: str
    file_type: FileType
    elements: list[DocumentElement] = field(default_factory=list)