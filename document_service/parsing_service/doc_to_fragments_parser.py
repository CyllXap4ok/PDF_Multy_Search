from document_service.parsing_service.strategy.parsing_strategy import ParsingStrategy


class DocumentParser:

    def __init__(self, strategy: ParsingStrategy = None):
        self.strategy = strategy

    def set_strategy(self, strategy: ParsingStrategy):
        self.strategy = strategy

    def parse_file(self, file_path: str, strategy: ParsingStrategy = None):
        if not strategy is None:
            self.strategy = strategy

        if self.strategy is None:
            raise AttributeError("Strategy is None")

        return self.strategy.parse_file(file_path)
