from abc import ABC, abstractmethod


class ConnectionInterface(ABC):
    @abstractmethod
    def connect(self) -> None:
        pass

    @abstractmethod
    def query(self, statement: str, params: list = None):
        pass

    @abstractmethod
    def close(self) -> None:
        pass
