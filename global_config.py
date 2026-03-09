import multiprocessing


class GlobalConfig:
    SEARCH_CONTEXT_LENGTH = 250
    SEARCH_MAX_PROCESSES = multiprocessing.cpu_count()