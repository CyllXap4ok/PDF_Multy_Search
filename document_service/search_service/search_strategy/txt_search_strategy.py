from typing import Callable

from document_service.document import Document
from document_service.search_service.search_match import SearchMatch
from document_service.search_service.search_strategy.search_strategy import SearchStrategy


class TxtSearchStrategy(SearchStrategy):
    def search(self, query: str, document: Document, context_length: int, progress_update: Callable[[float], None],
               matches_found: Callable[[list[SearchMatch]], None]) -> list[SearchMatch]:
        pass # TODO()