from src.Application.UseCases.use_case_interface import UseCaseInterface
from src.Infra.Http.interface_server_http import HttpServer


class MainController:
    def __init__(
        self,
        http_server: HttpServer,
        create_user: UseCaseInterface,
        deposit_amount: UseCaseInterface,
        create_transaction: UseCaseInterface,
    ) -> None:
        self.__create_user_use_case = create_user
        self.__deposit_amount_use_case = deposit_amount
        self.__create_transaction_use_case = create_transaction
        http_server.register("get", "/", self.__server)
        http_server.register("post", "/create-user", self.__create_user)
        http_server.register("post", "/deposit-amount", self.__deposit_amount)
        http_server.register("post", "/transaction", self.__create_transaction)

    def __server(self):
        return {"status_code": 200, "body": {"message": "Bem Vindo"}}

    def __create_user(self, req):
        output = self.__create_user_use_case.execute(req)
        return output

    def __deposit_amount(self, req):
        output = self.__deposit_amount_use_case.execute(req)
        return output

    def __create_transaction(self, req):
        output = self.__create_transaction_use_case.execute(req)
        return output
