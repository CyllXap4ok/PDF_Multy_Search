from __future__ import annotations

import multiprocessing
import queue
from typing import Callable, Any
from multiprocessing import Manager as MPManager

from document_service.document import Document
from document_service.search_service.search_match import SearchMatch
from document_service.search_service.search_strategy.search_strategy_fabric import SearchStrategyFabric
from global_config import GlobalConfig


class DocumentSearchProcessManager:

    def __init__(
            self,
            workers_num: int = None,
            document_search_started: Callable[[Document], None] = None,
            document_search_finished: Callable[[Document, list[SearchMatch]], None] = None,
            document_search_progress: Callable[[Document, int], None] = None,
            matches_found: Callable[[Document, list[SearchMatch]], None] = None
    ):
        self.callback_dict: dict[str, Callable] = {
            "document_search_started": document_search_started,
            "document_search_finished": document_search_finished,
            "document_search_progress": document_search_progress,
            "matches_found": matches_found
        }

        if workers_num is None: workers_num = multiprocessing.cpu_count()
        self.workers_num = workers_num

        self.mp_manager = MPManager()
        self.task_queue: multiprocessing.Queue[tuple[str, str]] = self.mp_manager.Queue()
        self.result_queue: multiprocessing.Queue[tuple[str, Any]] = self.mp_manager.Queue()
        self.processes: list[multiprocessing.Process] = []

    @staticmethod
    def __search_process_function__(
            task_queue: multiprocessing.Queue[tuple[str, str]],
            result_queue: multiprocessing.Queue[tuple[str, Any]]
    ):
        while True:
            task = task_queue.get()
            query, doc_path = task
            document = Document(doc_path)

            result_queue.put(("document_search_started", doc_path))

            search_strategy = SearchStrategyFabric.create(document)
            matches = search_strategy.search(
                query,
                document,
                GlobalConfig.SEARCH_CONTEXT_LENGTH,
                lambda progress: result_queue.put(("document_search_progress", (doc_path, int(progress)))),
                lambda new_matches: result_queue.put(("matches_found", (doc_path, [match.to_dict() for match in new_matches])))
            )

            result_queue.put(("document_search_finished", (doc_path, [match.to_dict() for match in matches])))

    def submit_tasks(self, query: str, documents: list[Document]):
        for doc in documents:
            task = (query, doc.file_path)
            self.task_queue.put(task)

    def handle_pending_results(self, timeout: float):
        while True:
            try:
                result = self.result_queue.get(timeout=timeout)
                self.handle_result(result)
            except queue.Empty:
                break

    def handle_result(self, result: tuple[str, Any]) -> None:
        callback_key, data = result
        callback = self.callback_dict[callback_key]

        if callback is None: return

        match callback_key:
            case "document_search_started":
                doc = Document(data)
                callback(doc)
            case "document_search_finished" | "matches_found":
                doc_path, transformed_matches = data
                doc = Document(doc_path)
                matches = [SearchMatch.from_dict(transformed_match) for transformed_match in transformed_matches]
                callback(doc, matches)
            case "document_search_progress":
                doc_path, progress = data
                doc = Document(doc_path)
                callback(doc, progress)

    def start_process_pool(self):
        for _ in range(self.workers_num):
            process = multiprocessing.Process(
                target=self.__search_process_function__,
                args=(self.task_queue, self.result_queue),
                daemon=True
            )
            process.start()
            self.processes.append(process)

    def stop_process_pool(self):
        for process in self.processes:
            process.terminate()

    def stop_searching(self):
        while not self.task_queue.empty():
            try:
                self.task_queue.get_nowait()
            except queue.Empty:
                break

    def set_workers_num(self, workers_num: int):
        self.workers_num = workers_num

    def set_document_search_started_callback(self, callback: Callable[[Document], None]):
        self.callback_dict["document_search_started"] = callback

    def set_document_search_finished_callback(self, callback: Callable[[Document, list[SearchMatch]], None]):
        self.callback_dict["document_search_finished"] = callback

    def set_document_search_progress_callback(self, callback: Callable[[Document, int], None]):
        self.callback_dict["document_search_progress"] = callback

    def set_matches_found_callback(self, callback: Callable[[Document, list[SearchMatch]], None]):
        self.callback_dict["matches_found"] = callback