import uuid
from src.Domain.VO.amount import Amount
from src.Domain.VO.email import Email
from src.Domain.VO.name import Name
from src.Domain.VO.password import Password
from src.Domain.VO.registration_number import RegistrationNumber
from src.Domain.VO.user_type import UserType


class User:
    def __init__(
        self,
        id: str,
        name: Name,
        email: Email,
        registration_number: RegistrationNumber,
        password: Password,
        amount: Amount,
        user_type: UserType,
    ) -> None:
        self.__id = id
        self.__name = name
        self.__email = email
        self.__registration_number = registration_number
        self.__password = password
        self.__amount_user = amount
        self.__user_type = user_type

    @staticmethod
    def create(
        name: str,
        email: str,
        registration_number: str,
        password: str,
        amount_user: float,
        user_type: str,
    ):
        user_id = uuid.uuid4()
        return User(
            user_id,
            Name(name),
            Email(email),
            RegistrationNumber(registration_number),
            Password.create(password),
            Amount(amount_user),
            UserType(user_type),
        )

    @staticmethod
    def restore(
        id: str,
        name: str,
        email: str,
        registration_number: str,
        password: str,
        amount_user: float,
        user_type: str,
    ):
        return User(
            id,
            Name(name),
            Email(email),
            RegistrationNumber(registration_number),
            Password(password),
            Amount(amount_user),
            UserType(user_type),
        )

    def to_dict(self):
        return {
            "id": str(self.__id),
            "amount": self.__amount_user.get_value(),
            "name": self.__name.get_value(),
            "email": self.__email.get_value(),
            "password": self.__password.get_value(),
            "registration_number": self.__registration_number.get_value(),
            "user_type": self.__user_type.get_value(),
        }

    def deposit(self, value: float):
        if value < 0:
            raise ValueError("The value cannot be negative")
        amount = self.__amount_user.get_value()
        amount += value
        self.set_amount(amount)
        return amount

    def transfer(self, value: float):
        if value < 0 or self.__amount_user.get_value() <= value:
            raise ValueError("It is not possible to transfer this amount")
        amount = self.__amount_user.get_value()
        amount -= value
        self.set_amount(amount)
        return amount

    def set_amount(self, value):
        self.__amount_user = value
        return self.__amount_user

    def get_id(self) -> str:
        return self.__id

    def get_amount(self) -> float:
        return self.__amount_user

    def get_name(self) -> str:
        return self.__name

    def get_email(self) -> str:
        return self.__email

    def get_registration_number(self) -> str:
        return self.__registration_number

    def get_user_type(self) -> str:
        return self.__user_type
