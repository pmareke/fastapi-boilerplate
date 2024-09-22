from expects import equal, expect
from doublex import Mimic, Stub
from src.infrastructure.hello.hello_client import DummyHelloClient
from src.use_cases.say_hello_command import SayHelloCommand, SayHelloCommandHandler


class TestSayHelloCommand:
    def test_execute(self) -> None:
        name = "John"
        command = SayHelloCommand(name)
        with Mimic(Stub, DummyHelloClient) as hello_client:
            hello_client.get(name).returns(name)
        handler = SayHelloCommandHandler(hello_client)

        response = handler.execute(command)

        expect(response.message()).to(equal(f"Hello, {name}!"))
