import pytest

from expects import expect, equal
from fastapi.testclient import TestClient
from http.client import OK
from main import app
from src.common import config


class TestHealthController:
    @pytest.fixture
    def client(self) -> TestClient:
        return TestClient(app)

    def test_health_controller(self, client: TestClient) -> None:
        response = client.get(f"{config.API_V1_PREFIX}/health")

        expect(response.status_code).to(equal(OK))
        expect(response.json()).to(equal({"ok": True}))
