from logging import Logger

from src.common.logger import logger
from src.domain.command import Command, CommandHandler, CommandResponse
from src.domain.exceptions import (
    SayHelloClientException,
    SayHelloCommandHandlerException,
)
from src.domain.hello_client import HelloClient


class SayHelloCommand(Command):
    def __init__(self, name: str):
        self.name = name
        super().__init__()


class SayHelloCommandResponse(CommandResponse):
    def __init__(self, name: str) -> None:
        self.name = name

    def message(self) -> str:
        return f"Hello, {self.name}!"


class SayHelloCommandHandler(CommandHandler):
    def __init__(self, hello_client: HelloClient, _logger: Logger = logger) -> None:
        self._hello_client = hello_client
        self._logger = _logger

    def execute(self, command: SayHelloCommand) -> SayHelloCommandResponse:
        command_id = command.command_id
        self._logger.info(f"Command {command_id}: HealthCommandHandler#execute")

        try:
            name = self._hello_client.get(command.name)
        except SayHelloClientException as ex:
            error_message = f"Command {command_id}: {ex}"
            raise SayHelloCommandHandlerException(error_message) from ex

        response = SayHelloCommandResponse(name)
        message = response.message()
        self._logger.info(f"Command {command_id}: SayHelloCommandResponse {message}")
        return response
