from src.domain.exceptions import SayHelloClientException
from src.domain.hello_client import HelloClient


class DummyHelloClient(HelloClient):
    def get(self, name: str) -> str:
        if name.startswith("Error"):
            raise SayHelloClientException(name)

        return name
