from src.Application.UseCases.use_case_interface import UseCaseInterface
from src.Infra.Http.interface_server_http import HttpServer


class MainController:
    def __init__(
        self,
        http_server: HttpServer,
        create_user: UseCaseInterface,
        deposit_amount: UseCaseInterface,
        create_transaction: UseCaseInterface,
        find_all_transactions: UseCaseInterface,
        find_transaction_id: UseCaseInterface,
        find_user_id: UseCaseInterface,
    ) -> None:
        self.__create_user_use_case = create_user
        self.__deposit_amount_use_case = deposit_amount
        self.__create_transaction_use_case = create_transaction
        self.__find_all_transactions = find_all_transactions
        self.__find_transaction_id = find_transaction_id
        self.__find_user_id = find_user_id
        http_server.register("get", "/", self.__server)
        http_server.register("post", "/create-user", self.__create_user)
        http_server.register("post", "/deposit-amount", self.__deposit_amount)
        http_server.register("post", "/transaction", self.__create_transaction)
        http_server.register("get", "/transactions", self.__transactions)
        http_server.register("get", "/transactions/<id>", self.__transaction_id)
        http_server.register("get", "/user/<id>", self.__user_id)

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

    def __transactions(self):
        output = self.__find_all_transactions.execute()
        return output

    def __transaction_id(self, req):
        output = self.__find_transaction_id.execute(req)
        return output

    def __user_id(self, req):
        output = self.__find_user_id.execute(req)
        return output
