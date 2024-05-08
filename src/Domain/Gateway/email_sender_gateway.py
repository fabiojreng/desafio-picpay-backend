from abc import ABC, abstractmethod
from src.Domain.Entities.user import User


class EmailSenderGatewayInterface(ABC):
    @abstractmethod
    def sender(self, to: User, from_: User, value: float):
        pass
