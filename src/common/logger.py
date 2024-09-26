import logging

from src.common.settings import settings


def setup_logging() -> None:
    logger = logging.getLogger(settings.logger_name)
    logger.setLevel(logging.INFO)

    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)

    format = "%(levelname)s: %(asctime)s - %(message)s"
    formatter = logging.Formatter(format)

    ch.setFormatter(formatter)
    logger.addHandler(ch)
