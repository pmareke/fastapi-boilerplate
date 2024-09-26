from logging import INFO, Formatter, Logger, StreamHandler, getLogger

from src.common.settings import settings


def setup_logging() -> Logger:
    log_format = "%(levelname)s: %(asctime)s - %(message)s"
    formatter = Formatter(log_format)

    handler = StreamHandler()
    handler.setLevel(INFO)
    handler.setFormatter(formatter)

    _logger = getLogger(settings.logger_name)
    _logger.setLevel(INFO)
    _logger.addHandler(handler)
    return _logger


logger = setup_logging()
