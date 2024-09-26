from logging import INFO, Formatter, Logger, StreamHandler, getLogger

from src.common.settings import settings


def setup_logging() -> Logger:
    format = "%(levelname)s: %(asctime)s - %(message)s"
    formatter = Formatter(format)

    handler = StreamHandler()
    handler.setLevel(INFO)
    handler.setFormatter(formatter)

    logger = getLogger(settings.logger_name)
    logger.setLevel(INFO)
    logger.addHandler(handler)
    return logger


logger = setup_logging()
