from src.Application.UseCases.use_case_interface import UseCaseInterface
from src.Domain.Entities.user import User
from src.Domain.Helpers.http_helper import (
    HttpResponse,
    forbidden,
    not_found,
    success,
    unprocessable_entity,
    server_error,
)
from src.Domain.Repository.user_repository import UserRepositoryInterface


class DepositAmountUseCase(UseCaseInterface):
    def __init__(self, user_repository: UserRepositoryInterface) -> None:
        self.__user_repository = user_repository

    def execute(self, params: any) -> HttpResponse:
        try:
            user = self.__user_repository.find_by_registration_number(
                params.get("registration_number")
            )

            if not user:
                return not_found("User do not exists")

            amount = user.deposit(params.get("value"))

            self.__user_repository.update_amount(amount, params["registration_number"])

            return success({"message": "Deposit successful", "data": {"value": amount}})
        except Exception as e:
            if isinstance(e, Exception):
                return unprocessable_entity(str(e))
            return server_error("Unexpected Error")
