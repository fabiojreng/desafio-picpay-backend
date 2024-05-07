from abc import ABC, abstractmethod

from src.Domain.Helpers.http_helper import HttpResponse


class AuthorizationDecoratorInterface(ABC):
    @abstractmethod
    def execute(self) -> HttpResponse:
        pass
