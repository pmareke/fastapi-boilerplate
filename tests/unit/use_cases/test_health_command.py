from expects import be_true, expect

from src.use_cases.health_command import HealthCommand, HealthCommandHandler


class TestHealthCommandHandler:
    def test_execute(self) -> None:
        command = HealthCommand()
        handler = HealthCommandHandler()

        response = handler.execute(command)

        expect(response.message()).to(be_true)
