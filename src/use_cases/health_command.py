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
        command_id = command.command_id
        self._logger.info(f"Command {command_id}: HealthCommandHandler#execute")

        response = HealthCommandResponse(command)
        message = response.message()
        self._logger.info(f"Command {command_id}: HealthCommandResponse {message}")
        return response
