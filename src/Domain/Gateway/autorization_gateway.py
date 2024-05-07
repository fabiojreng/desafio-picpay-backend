from abc import ABC, abstractmethod


class AuthorizationGatewayInterface(ABC):
    @abstractmethod
    def authorization(self):
        pass
