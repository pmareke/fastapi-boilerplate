import logging
from logging import INFO

from src.common.settings import settings


def setup_logging() -> None:
    ch = logging.StreamHandler()
    ch.setLevel(INFO)

    format = "%(levelname)s: %(asctime)s - %(message)s"
    formatter = logging.Formatter(format)
    ch.setFormatter(formatter)

    logger = logging.getLogger(settings.logger_name)
    logger.setLevel(INFO)
    logger.addHandler(ch)
