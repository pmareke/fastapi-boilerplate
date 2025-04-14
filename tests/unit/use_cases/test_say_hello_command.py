from doublex import Mimic, Stub
from expects import equal, expect, raise_error

from src.domain.exceptions import (
    SayHelloClientException,
    SayHelloCommandHandlerException,
)
from src.infrastructure.hello.hello_client import DummyHelloClient
from src.use_cases.say_hello_command import SayHelloCommand, SayHelloCommandHandler


class TestSayHelloCommandHandler:
    def test_execute(self) -> None:
        name = "John"
        command = SayHelloCommand(name)
        with Mimic(Stub, DummyHelloClient) as hello_client:
            hello_client.get(name).returns(name)
        handler = SayHelloCommandHandler(hello_client)  # type: ignore

        response = handler.execute(command)

        expect(response.message()).to(equal(f"Hello, {name}!"))

    def test_raise_exception(self) -> None:
        name = "John"
        command = SayHelloCommand(name)
        with Mimic(Stub, DummyHelloClient) as hello_client:
            hello_client.get(name).raises(SayHelloClientException(name))
        handler = SayHelloCommandHandler(hello_client)  # type: ignore

        error_message = f"Command {command.command_id}: '{name}' invalid name"
        expect(lambda: handler.execute(command)).to(raise_error(SayHelloCommandHandlerException, error_message))
