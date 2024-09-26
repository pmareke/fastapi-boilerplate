import logging


def setup_logging() -> None:
    logger = logging.getLogger("server")
    logger.setLevel(logging.INFO)
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    format = "%(levelname)s: %(asctime)s - %(message)s"
    formatter = logging.Formatter(format)
    ch.setFormatter(formatter)
    logger.addHandler(ch)
