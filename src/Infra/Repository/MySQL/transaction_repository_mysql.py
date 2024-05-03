from src.Domain.Entities.transaction import Transaction
from src.Domain.Repository.transaction_repository import TransactionRepositoryInterface
from src.Infra.DataBase.connection_mysql import ConnectionMySql


class TransactionRepositoryMySQL(TransactionRepositoryInterface):
    def __init__(self, mysql: ConnectionMySql):
        self.__mysql = mysql

    def save_transaction(self, transaction: dict) -> None:
        self.__mysql.connect()
        self.__mysql.query(
            "INSERT INTO transactions (id, payer, payee, value) VALUES (%s, %s, %s, %s)",
            [
                transaction["id"],
                transaction["payer"]["name"],
                transaction["payee"]["name"],
                transaction["value"],
            ],
        )
        self.__mysql.close()

    def find_transaction_id(self, id: str) -> list:
        self.__mysql.connect()
        transaction = self.__mysql.query(
            "SELECT * FROM transactions WHERE id = %s", [id]
        )

        if not transaction:
            return None
        (
            transaction_id,
            transaction_payer,
            transaction_payee,
            transaction_value,
        ) = transaction[0]

        output = Transaction.restore(
            transaction_id, transaction_payer, transaction_payee, transaction_value
        )

        self.__mysql.close()
        return output

    def find_all_transactions(self) -> list[dict]:
        return super().find_all_transactions()
