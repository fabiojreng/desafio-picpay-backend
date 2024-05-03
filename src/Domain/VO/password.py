import hashlib


class Password:
    def __init__(self, password: str) -> None:
        self.__value = password

    @staticmethod
    def create(password: str):
        password = password.replace(" ", "")
        if len(password) < 8:
            raise ValueError("Invalid password")
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        return Password(hashed_password)

    def validate(self, password: str) -> bool:
        hashed_input = hashlib.sha256(password.encode()).hexdigest()
        return hashed_input == self.__value

    def get_value(self) -> str:
        return self.__value
