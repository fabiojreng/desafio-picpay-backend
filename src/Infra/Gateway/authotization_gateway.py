from src.Domain.Gateway.autorization_gateway import AuthorizationGatewayInterface
from src.Infra.Http.interface_client_http import HttpClientInterface


class AuthorizationGateway(AuthorizationGatewayInterface):
    def __init__(self, http_client: HttpClientInterface) -> None:
        self.__http_client = http_client

    def authorization(self):
        # return {"status": 200, "data": {"message": "Não autorizado"}}
        return self.__http_client.get(
            "https://run.mocky.io/v3/5794d450-d2e2-4412-8131-73d0293ac1cc"
        )
