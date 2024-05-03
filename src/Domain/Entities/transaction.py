import uuid
from src.Domain.Entities.user import User


class Transaction:
    def __init__(
        self,
        id: str,
        payer: str,
        payee: str,
        value: float,
    ) -> None:
        self.__id = id
        self.__payer = payer
        self.__payee = payee
        self.__value = value

    @staticmethod
    def create(payer: User, payee: User, value: str):
        if payer.get_user_type() != "Common":
            raise ValueError("Only common user can make transfer")
        if payer.get_amount() < 0:
            raise ValueError("No balance to transfer")
        id = uuid.uuid4()

        return Transaction(id, payer, payee, value)

    def to_dict(self):
        return {
            "id": str(self.__id),
            "payer": self.__payer,
            "payee": self.__payee,
            "value": self.__value,
        }

    def get_id(self):
        return self.__id

    def get_payer(self):
        return self.__payer

    def get_payee(self):
        return self.__payee

    def get_value(self):
        return self.__value
