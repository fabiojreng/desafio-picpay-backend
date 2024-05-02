from abc import ABC, abstractmethod


class HttpServer(ABC):
    @abstractmethod
    def register(self, method, url: str, callback):
        pass

    @abstractmethod
    def listen(self, port):
        pass
