from abc import ABC, abstractmethod

from src.Domain.Entities.transaction import Transaction


class TransactionRepositoryInterface(ABC):
    @abstractmethod
    def save_transaction(self, transaction: dict) -> None:
        pass

    @abstractmethod
    def find_transaction_id(self, id: str) -> list:
        pass

    @abstractmethod
    def find_all_transactions(self) -> list[dict]:
        pass
