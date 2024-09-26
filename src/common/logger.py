from logging import INFO, Formatter, StreamHandler, getLogger

from src.common.settings import settings


def setup_logging() -> None:
    format = "%(levelname)s: %(asctime)s - %(message)s"
    formatter = Formatter(format)

    handler = StreamHandler()
    handler.setLevel(INFO)
    handler.setFormatter(formatter)

    logger = getLogger(settings.logger_name)
    logger.setLevel(INFO)
    logger.addHandler(handler)
