import logging

from logging import Logger
from src.domain.command import Command, CommandHandler, CommandResponse
from src.domain.hello_client import HelloClient


class SayHelloCommand(Command):
    def __init__(self, name: str):
        self.name = name
        super().__init__()


class SayHelloCommandResponse(CommandResponse):
    def __init__(self, command: SayHelloCommand, name: str) -> None:
        self.command = command
        self.name = name

    def message(self) -> str:
        return f"Hello, {self.name}!"


class SayHelloCommandHandler(CommandHandler):
    def __init__(
        self,
        hello_client: HelloClient,
        logger: Logger = logging.getLogger(__name__),
    ) -> None:
        self._hello_client = hello_client
        self._logger = logger

    def execute(self, command: SayHelloCommand) -> SayHelloCommandResponse:
        command_id = command.command_id
        self._logger.info(f"Command {command_id}: HealthCommandHandler#execute")

        name = self._hello_client.get(command.name)
        response = SayHelloCommandResponse(command, name)
        message = response.message()
        self._logger.info(f"Command {command_id}: SayHelloCommandResponse {message}")
        return response
