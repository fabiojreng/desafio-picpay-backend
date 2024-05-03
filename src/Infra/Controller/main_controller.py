from src.Application.UseCases.use_case_interface import UseCaseInterface
from src.Infra.Http.interface_server_http import HttpServer


class MainController:
    def __init__(
        self,
        http_server: HttpServer,
        create_user: UseCaseInterface,
    ) -> None:
        self.__create_user_use_case = create_user
        http_server.register("get", "/", self.__server)
        http_server.register("post", "/create-user", self.__create_user)

    def __server(self):
        return {"status_code": 200, "body": {"message": "Bem Vindo"}}

    def __create_user(self, req):
        output = self.__create_user_use_case.execute(req)
        return output
