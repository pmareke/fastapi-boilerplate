from http.client import OK

import pytest
from expects import equal, expect
from fastapi.testclient import TestClient

from main import app, settings


class TestHealthControllerAcceptance:
    @pytest.fixture
    def client(self) -> TestClient:
        return TestClient(app)

    def test_health_controller(self, client: TestClient) -> None:
        response = client.get(f"{settings.api_v1_prefix}/health")

        expect(response.status_code).to(equal(OK))
        expect(response.json()).to(equal({"ok": True}))
