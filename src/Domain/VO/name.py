import re


class Name:
    def __init__(self, name: str) -> None:
        if not re.match(r"^[A-Za-zÀ-ÖØ-öø-ÿ\s\'-]+$", name):
            raise ValueError("Invalid name")
        self._value = name

    def get_value(self) -> str:
        return self._value
