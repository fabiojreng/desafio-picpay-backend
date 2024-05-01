import re


class Email:
    def __init__(self, email: str) -> None:
        if not re.match(r"^(.+)@(.+)$", email):
            raise ValueError("Invalid email")
        self._value = email

    def get_value(self) -> str:
        return self._value
