from src.Application.UseCases.use_case_interface import UseCaseInterface
from src.Domain.Helpers.http_helper import (
    HttpResponse,
    no_content,
    server_error,
    success,
)
from src.Domain.Repository.transaction_repository import TransactionRepositoryInterface


class FindAllTransactionsUseCase(UseCaseInterface):
    def __init__(self, transaction_repository: TransactionRepositoryInterface) -> None:
        self.__transaction_repository = transaction_repository

    def execute(self, params: any = None) -> HttpResponse:
        try:
            transactions = self.__transaction_repository.find_all_transactions()
            if not transactions:
                return no_content()
            return success({"message": "Transactions list", "data": transactions})
        except Exception as e:
            if isinstance(e, Exception):
                return server_error(str(e))
            return server_error("Unexpected Error")
