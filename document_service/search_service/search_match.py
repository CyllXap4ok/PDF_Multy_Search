from dataclasses import dataclass

from document_service.document import Document


@dataclass
class MatchContext:
    before: str
    after: str


@dataclass
class SearchMatch:
    query: str
    context: MatchContext
    from_document: Document
    document_page: int

    def to_dict(self) -> dict:
        return {
            "query": self.query,
            "context": {
                "before": self.context.before,
                "after": self.context.after,
            },
            "from_document": self.from_document.file_path,
            "document_page": self.document_page
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            query=data["query"],
            context=MatchContext(data["context"]["before"], data["context"]["after"]),
            from_document=Document(data["from_document"]),
            document_page=data["document_page"]
        )
