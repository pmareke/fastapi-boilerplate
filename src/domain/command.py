import logging
import uuid

from abc import ABC, abstractmethod
from logging import Logger
from typing import Any


class Command:
    def __init__(self) -> None:
        self.command_id = uuid.uuid1()


class CommandResponse(ABC):
    @abstractmethod
    def message(self) -> Any:
        raise NotImplementedError()


class CommandHandler(ABC):
    def __init__(self, logger: Logger = logging.getLogger(__name__)) -> None:
        self._logger = logger

    @abstractmethod
    def execute(self, command: Command) -> CommandResponse:
        raise NotImplementedError()
