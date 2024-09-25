from expects import equal, expect, raise_error

from src.domain.exceptions import SayHelloClientException
from src.infrastructure.hello.hello_client import DummyHelloClient


class TestDummyHelloClientIntegration:
    def test_get_name(self) -> None:
        expected_name = "Yes"
        client = DummyHelloClient()

        name = client.get(expected_name)

        expect(name).to(equal(expected_name))

    def test_raise_error(self) -> None:
        expected_name = "Error"
        client = DummyHelloClient()

        error_message = f"'{expected_name}' invalid name"
        expect(lambda: client.get(expected_name)).to(
            raise_error(SayHelloClientException, error_message)
        )
