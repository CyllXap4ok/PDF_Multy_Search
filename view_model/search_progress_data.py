from dataclasses import dataclass


@dataclass
class SearchProgress:
    current_file: str = ""
    current_file_num: int = 0
    files_count: int = 0

    def set_current_file(self, current_file: str):
        self.current_file = current_file

    def increment_file_num(self):
        self.current_file_num += 1

    def set_files_count(self, files_count: int):
        self.files_count = files_count

    def clear_progress(self):
        self.current_file = ""
        self.current_file_num = 0
        self.files_count = 0

    def to_string(self) -> str:
        progress_percent = int(self.current_file_num / self.files_count * 100)
        return f"{progress_percent}% ({self.current_file_num}/{self.files_count}) [{self.current_file}]"