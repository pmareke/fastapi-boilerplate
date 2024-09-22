from src.domain.hello_client import HelloClient


class DummyHelloClient(HelloClient):
    def get(self, name: str) -> str:
        return name
