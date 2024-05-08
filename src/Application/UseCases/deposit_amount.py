from src.Application.UseCases.use_case_interface import UseCaseInterface
from src.Domain.Decorator.authorization import AuthorizationDecoratorInterface
from src.Domain.Helpers.http_helper import (
    HttpResponse,
    not_found,
    success,
    unauthorized,
    unprocessable_entity,
    server_error,
)
from src.Domain.Repository.user_repository import UserRepositoryInterface


class DepositAmountUseCase(UseCaseInterface):
    def __init__(
        self,
        user_repository: UserRepositoryInterface,
        authorization: AuthorizationDecoratorInterface,
    ) -> None:
        self.__user_repository = user_repository
        self.__authorization = authorization

    def execute(self, params: any = None) -> HttpResponse:
        try:
            user = self.__user_repository.find_by_registration_number(
                params.get("registration_number")
            )

            if not user:
                return not_found("User do not exists")

            authorization = self.__authorization.execute()
            if authorization["status"] != "Authorized":
                return unauthorized("Deposit unauthorized")

            amount = user.deposit(params.get("value"))

            self.__user_repository.update_amount(amount, params["registration_number"])

            return success({"message": "Deposit successful", "data": {"value": amount}})
        except Exception as e:
            if isinstance(e, Exception):
                return unprocessable_entity(str(e))
            return server_error("Unexpected Error")
