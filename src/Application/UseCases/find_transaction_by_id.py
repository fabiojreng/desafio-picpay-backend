from src.Application.UseCases.use_case_interface import UseCaseInterface
from src.Domain.Helpers.http_helper import (
    HttpResponse,
    no_content,
    server_error,
    success,
    unprocessable_entity,
)
from src.Domain.Repository.transaction_repository import TransactionRepositoryInterface


class FindTransactionByIdUseCase(UseCaseInterface):
    def __init__(self, transaction_repository: TransactionRepositoryInterface) -> None:
        self.__transaction_repository = transaction_repository

    def execute(self, params: any = None) -> HttpResponse:
        try:
            transaction = self.__transaction_repository.find_transaction_id(
                params.get("id")
            )
            if not transaction:
                return no_content()
            return success({"message": "Transaction", "data": transaction.to_dict()})
        except Exception as e:
            if isinstance(e, Exception):
                return unprocessable_entity(str(e))
            return server_error("Unexpected Error")
