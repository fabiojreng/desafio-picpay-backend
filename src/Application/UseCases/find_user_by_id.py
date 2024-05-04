from src.Application.UseCases.use_case_interface import UseCaseInterface
from src.Domain.Helpers.http_helper import (
    HttpResponse,
    no_content,
    server_error,
    success,
    unprocessable_entity,
)
from src.Domain.Repository.user_repository import UserRepositoryInterface


class FindUserByIdUseCase(UseCaseInterface):
    def __init__(self, user_repository: UserRepositoryInterface) -> None:
        self.__user_repository = user_repository

    def execute(self, params: any = None) -> HttpResponse:
        try:
            user = self.__user_repository.find_by_id(params.get("id"))
            if not user:
                return no_content()
            user = user.to_dict()
            return success(
                {
                    "message": "User",
                    "data": {
                        "amount": user["amount"],
                        "name": user["name"],
                        "email": user["email"],
                        "user_type": user["user_type"],
                    },
                }
            )
        except Exception as e:
            if isinstance(e, Exception):
                return unprocessable_entity(str(e))
            return server_error("Unexpected Error")
