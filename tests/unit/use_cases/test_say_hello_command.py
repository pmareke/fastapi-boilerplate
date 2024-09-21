from expects import equal, expect
from src.use_cases.say_hello_command import SayHelloCommand, SayHelloCommandHandler


class TestSayHelloCommand:
    def test_execute(self) -> None:
        name = "John"
        command = SayHelloCommand(name)
        handler = SayHelloCommandHandler()

        response = handler.execute(command)

        expect(response.message()).to(equal(f"Hello, {name}!"))
