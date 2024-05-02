from abc import ABC, abstractmethod
from src.Domain.Helpers.http_helper import HttpResponse


class UseCaseInterface(ABC):
    @abstractmethod
    def execute(self, params: any) -> HttpResponse:
        pass
