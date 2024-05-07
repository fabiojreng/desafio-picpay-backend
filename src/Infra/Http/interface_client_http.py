from abc import ABC, abstractmethod


class HttpClientInterface(ABC):

    def get(url: str):
        pass

    def post(url: str, data: dict):
        pass
