class SayHelloClientException(Exception):
    def __init__(self, name: str) -> None:
        super().__init__(f"'{name}' invalid name")


class SayHelloCommandHandlerException(Exception):
    def __init__(self, error: str) -> None:
        super().__init__(error)
