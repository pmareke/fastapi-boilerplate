import pytest

from doublex import ANY_ARG, Mimic, Stub
from expects import expect, equal
from fastapi.testclient import TestClient
from http.client import INTERNAL_SERVER_ERROR
from main import app
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

    @pytest.fixture
    def client(self) -> TestClient:
        return TestClient(app)

    def test_hello_controller(self, client: TestClient) -> None:
        app.dependency_overrides[say_hello_command_handler] = self._failing_handler
        name = "peter"

        response = client.get(f"/api/v1/hello/{name}")

        expect(response.status_code).to(equal(INTERNAL_SERVER_ERROR))
        expect(response.json()).to(equal({"detail": self.ERROR_MESSAGE}))
