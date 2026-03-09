from typing import Callable

import pymupdf

from document_service.document import Document
from document_service.search_service.search_match import SearchMatch
from document_service.search_service.search_strategy.search_strategy import SearchStrategy


class PdfSearchStrategy(SearchStrategy):

    def __init__(self):
        super().__init__()

    def search(
            self,
            query: str,
            document: Document,
            context_length: int,
            progress_update: Callable[[float], None],
            matches_found: Callable[[list[SearchMatch]], None]
    ) -> list[SearchMatch]:

        query_length = len(query)
        if query_length == 0: raise ValueError("Query is empty")

        matches: list[SearchMatch] = []
        shifts: dict[str, int] = {query[i]: max(1, query_length - i - 1) for i in range(query_length)}

        try:
            with pymupdf.open(document.file_path) as doc:
                for page_index in range(len(doc)):
                    page = doc[page_index]
                    text = page.get_text()
                    match_indexes = self.__boyer_moore_search__(query, text, shifts)

                    new_matches: list[SearchMatch] = []
                    for index in match_indexes:
                        context = self.__get_context__(text, index, query_length, context_length)
                        match = SearchMatch(query, context, document, page_index+1)
                        new_matches.append(match)

                    if len(new_matches) > 0:
                        matches_found(new_matches)
                        matches.extend(new_matches)

                    progress = (page_index + 1) / len(doc) * 100
                    progress_update(progress)

        except ValueError:
            pass

        return matches