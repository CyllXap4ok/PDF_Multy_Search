import pymupdf

from document_service.parsing_service.doc_fragment import DocumentFragment, DocumentElement, ElementType, DocElementMetadataType
from document_service.document import FileType
from document_service.parsing_service.strategy.parsing_strategy import ParsingStrategy


class PDFParsingStrategy(ParsingStrategy):
    """
    Пока что парсинг не учитывает наличие картинок. Далее, скорее всего, надо будет использовать
    другую библиотеку для работы с pdf и парсить картинки. Картинки будут передаваться нейронке
    OCR, которая будет переводить их в текст.
    """

    fragment_pages = 5

    def parse_file(self, file_path) -> list[DocumentFragment]:
        fragments: list[DocumentFragment] = []

        try:
            with pymupdf.open(file_path) as doc:
                doc_fragment = DocumentFragment(file_path, FileType.PDF)

                for page_num in range(len(doc)):
                    page = doc[page_num]
                    text = page.get_text()

                    doc_element = DocumentElement(
                        content=text,
                        element_type=ElementType.PARAGRAPH,
                        metadata={DocElementMetadataType.PAGE_NUMBER: page_num}
                    )

                    doc_fragment.elements.append(doc_element)

                    if (page_num + 1) % self.fragment_pages == 0:
                        fragments.append(doc_fragment)
                        doc_fragment = DocumentFragment(file_path, FileType.PDF)

                if doc_fragment.elements:
                    fragments.append(doc_fragment)

        except FileNotFoundError:
            raise FileNotFoundError(f"File {file_path} not found.")

        return fragments