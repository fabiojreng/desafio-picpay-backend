from src.Domain.Decorator.authorization import AuthorizationDecoratorInterface
from src.Domain.Gateway.autorization_gateway import AuthorizationGatewayInterface
from src.Domain.Helpers.http_helper import HttpResponse


class AutenticatorAuthorizationDecorator(AuthorizationDecoratorInterface):
    def __init__(self, authorization_gateway: AuthorizationGatewayInterface) -> None:
        self.__authorization_gateway = authorization_gateway

    def execute(self) -> HttpResponse:
        try:
            response = self.__authorization_gateway.authorization()
            print(response)
            if response["data"]["message"] == "Autorizado":
                return {"status": "Authorized", "data": ""}
            return {"status": "Denied", "data": ""}
        except Exception as e:
            return {"status": "Denied", "data": str(e)}
