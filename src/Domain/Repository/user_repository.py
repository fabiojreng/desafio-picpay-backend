from abc import ABC, abstractmethod

from src.Domain.Entities.user import User


class UserRepositoryInterface(ABC):
    @abstractmethod
    def save_user(self, user: dict) -> None:
        pass

    @abstractmethod
    def find_by_registration_number(self, registration: str) -> User:
        pass

    @abstractmethod
    def find_by_email(self, email: str) -> User:
        pass

    @abstractmethod
    def update_amount(self, value: float, registration_number: str) -> None:
        pass
