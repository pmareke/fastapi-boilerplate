import pytest

from expects import expect, equal
from fastapi.testclient import TestClient
from http.client import OK
from main import app
from src.common import config


class TestHelloController:
    @pytest.fixture
    def client(self) -> TestClient:
        return TestClient(app)

    def test_hello_controller(self, client: TestClient) -> None:
        name = "peter"

        response = client.get(f"{config.API_V1_PREFIX}/hello/{name}")

        expect(response.status_code).to(equal(OK))
        expect(response.json()).to(equal({"message": f"Hello, {name}!"}))
