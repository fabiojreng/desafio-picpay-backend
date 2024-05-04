from src.Application.UseCases.use_case_interface import UseCaseInterface
from src.Domain.Entities.transaction import Transaction
from src.Domain.Helpers.http_helper import (
    HttpResponse,
    created,
    not_found,
    server_error,
    unprocessable_entity,
)
from src.Domain.Repository.transaction_repository import TransactionRepositoryInterface
from src.Domain.Repository.user_repository import UserRepositoryInterface


class CreateTransactionUseCase(UseCaseInterface):
    def __init__(
        self,
        transaction_repository: TransactionRepositoryInterface,
        user_repository: UserRepositoryInterface,
    ) -> None:
        self.__transaction_repository = transaction_repository
        self.__user_repository = user_repository

    def execute(self, params: any = None) -> HttpResponse:
        try:
            payer = self.__user_repository.find_by_registration_number(
                params.get("registration_number_payer")
            )
            if not payer:
                return not_found("Payer not found")
            payee = self.__user_repository.find_by_registration_number(
                params.get("registration_number_payee")
            )
            if not payee:
                return not_found("Payee not found")

            transaction = Transaction.create(
                payer.to_dict(), payee.to_dict(), params.get("value")
            ).to_dict()

            amount_payee = payee.deposit(params.get("value"))
            amount_payer = payer.transfer(params.get("value"))

            self.__user_repository.update_amount(
                amount_payee, params.get("registration_number_payee")
            )
            self.__user_repository.update_amount(
                amount_payer, params.get("registration_number_payer")
            )
            self.__transaction_repository.save_transaction(transaction)

            return created(
                {
                    "message": "Transaction successfully",
                    "data": {
                        "id": transaction["id"],
                        "payer": transaction["payer"]["name"],
                        "payee": transaction["payee"]["name"],
                        "value": transaction["value"],
                    },
                }
            )
        except Exception as e:
            if isinstance(e, Exception):
                return unprocessable_entity(str(e))
            return server_error("Unexpected Error")
