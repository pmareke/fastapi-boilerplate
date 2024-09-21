from src.domain.command import Command, CommandHandler, CommandResponse


class HealthCommand(Command):
    def __init__(self) -> None:
        super().__init__()


class HealthCommandResponse(CommandResponse):
    def __init__(self, command: HealthCommand) -> None:
        self.command = command

    def message(self) -> bool:
        return True


class HealthCommandHandler(CommandHandler):
    def execute(self, command: HealthCommand) -> HealthCommandResponse:
        self._logger.info(f"Command {command.command_id}: HealthCommandHandler#execute")
        say_hello_command_response = HealthCommandResponse(command)
        self._logger.info(
            f"Command {command.command_id}: HealthCommandResponse {say_hello_command_response.message()}"
        )
        return say_hello_command_response
