from abc import ABC, abstractmethod


class HelloClient(ABC):
    @abstractmethod
    def get(self, name: str) -> str:
        raise NotImplementedError
