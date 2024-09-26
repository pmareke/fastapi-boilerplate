import logging
from logging import INFO

from src.common.settings import settings


def setup_logging() -> None:
    handler = logging.StreamHandler()
    handler.setLevel(INFO)

    format = "%(levelname)s: %(asctime)s - %(message)s"
    formatter = logging.Formatter(format)
    handler.setFormatter(formatter)

    logger = logging.getLogger(settings.logger_name)
    logger.setLevel(INFO)
    logger.addHandler(handler)
