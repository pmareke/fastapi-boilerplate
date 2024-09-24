from doublex import ANY_ARG, Mimic, Stub
from expects import expect, equal
from fastapi.testclient import TestClient
from http.client import BAD_REQUEST
from main import app, settings
from src.delivery.api.v1.hello.hello_router import say_hello_command_handler
from src.domain.exceptions import SayHelloCommandHandlerException
from src.use_cases.say_hello_command import SayHelloCommandHandler


class TestHelloController:
    ERROR_MESSAGE = "any error message"

    def _failing_handler(self) -> SayHelloCommandHandler:
        with Mimic(Stub, SayHelloCommandHandler) as self.handler:
            exception = SayHelloCommandHandlerException(self.ERROR_MESSAGE)
            self.handler.execute(ANY_ARG).raises(exception)
        return self.handler  # type: ignore

    def test_hello_controller(self) -> None:
        client = TestClient(app)
        app.dependency_overrides[say_hello_command_handler] = self._failing_handler
        invalid_name = "any-invalid-name"

        response = client.get(f"{settings.api_v1_prefix}/hello/{invalid_name}")

        expect(response.status_code).to(equal(BAD_REQUEST))
        expect(response.json()).to(equal({"detail": self.ERROR_MESSAGE}))
