from src.domain.command import Command, CommandHandler, CommandResponse


class SayHelloCommand(Command):
    def __init__(self, name: str):
        self.name = name
        super().__init__()


class SayHelloCommandResponse(CommandResponse):
    def __init__(self, command: SayHelloCommand) -> None:
        self.command = command

    def message(self) -> str:
        return f"Hello, {self.command.name}!"


class SayHelloCommandHandler(CommandHandler):
    def execute(self, command: SayHelloCommand) -> SayHelloCommandResponse:
        command_id = command.command_id
        self._logger.info(f"Command {command_id}: HealthCommandHandler#execute")

        response = SayHelloCommandResponse(command)
        message = response.message()
        self._logger.info(f"Command {command_id}: SayHelloCommandResponse {message}")
        return response
