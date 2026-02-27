class PDFOccurrence:

    def __init__(
            self,
            context: str,
            start_position: int,
            end_position: int,
            page_number: int
    ):
        self.context = context
        self.start_position = start_position
        self.end_position = end_position
        self.page_number = page_number
