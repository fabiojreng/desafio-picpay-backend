from src.Application.UseCases.use_case_interface import UseCaseInterface
from src.Domain.Entities.user import User
from src.Domain.Helpers.http_helper import (
    HttpResponse,
    created,
    server_error,
    unprocessable_entity,
)
from src.Domain.Repository.user_repository import UserRepositoryInterface


class CreateUserUseCase(UseCaseInterface):
    def __init__(self, user_repository: UserRepositoryInterface) -> None:
        self.__user_repository = user_repository

    def execute(self, params: any = None) -> HttpResponse:
        try:
            registration_number_exists = (
                self.__user_repository.find_by_registration_number(
                    params.get("registration_number")
                )
            )
            if registration_number_exists:
                return unprocessable_entity(
                    "There is already a user with this registration number"
                )

            email_exists = self.__user_repository.find_by_email(params.get("email"))
            if email_exists:
                return unprocessable_entity("There is already a user with this email")

            user = User.create(
                params.get("name"),
                params.get("email"),
                params.get("registration_number"),
                params.get("password"),
                params.get("amount_user"),
                params.get("user_type"),
            ).to_dict()
            self.__user_repository.save_user(user)
            return created(
                {
                    "message": "User created successfully",
                    "data": {
                        "id": user.get("id"),
                        "name": user.get("name"),
                        "email": user.get("email"),
                        "user_type": user.get("user_type"),
                        "amount": user.get("amount"),
                    },
                }
            )

        except Exception as e:
            if isinstance(e, Exception):
                return unprocessable_entity(str(e))
            return server_error("Unexpected Error")
