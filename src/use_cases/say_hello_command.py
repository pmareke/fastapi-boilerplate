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
        self._logger.info(f"Command {command.command_id}: HealthCommandHandler#execute")
        say_hello_command_response = SayHelloCommandResponse(command)
        self._logger.info(
            f"Command {command.command_id}: SayHelloCommandResponse {say_hello_command_response.message()}"
        )
        return say_hello_command_response
