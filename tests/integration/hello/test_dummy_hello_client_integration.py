from expects import equal, expect
from src.infrastructure.hello.hello_client import DummyHelloClient


class TestDummyHelloClientIntegrtion:
    def test_get_name(self) -> None:
        expected_name = "Yes"
        client = DummyHelloClient()

        name = client.get(expected_name)

        expect(name).to(equal(expected_name))
