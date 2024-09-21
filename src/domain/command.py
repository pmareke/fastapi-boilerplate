from logging import Logger
import uuid

from abc import ABC, abstractmethod
from main import logger
from typing import Any


class Command:
    def __init__(self) -> None:
        self.command_id = uuid.uuid1()


class CommandResponse(ABC):
    @abstractmethod
    def message(self) -> Any:
        raise NotImplementedError()


class CommandHandler(ABC):
    def __init__(self, logger: Logger = logger) -> None:
        self._logger = logger

    @abstractmethod
    def execute(self, command: Command) -> CommandResponse:
        raise NotImplementedError()
