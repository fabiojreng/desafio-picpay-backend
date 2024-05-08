from src.Domain.Entities.user import User
from src.Domain.Gateway.email_sender_gateway import EmailSenderGatewayInterface
from src.Infra.Http.interface_client_http import HttpClientInterface


class EmailSenderGateway(EmailSenderGatewayInterface):
    def __init__(self, http_client: HttpClientInterface) -> None:
        self.__http_client = http_client

    def sender(self, to: User, from_: User, value: float):
        email_content = {
            "from": from_.get_name(),
            "to": to.get_name(),
            "message": f"Olá, {to.get_name()}. Você recebeu uma tranferência de {from_.get_name()} no valor de R$ ${value}",
        }
        response = self.__http_client.get(
            "https://run.mocky.io/v3/54dc2cf1-3add-45b5-b5a9-6bf7e7f1f4a6"
        )
        print(response, email_content)
        return response, email_content
