import re


class RegistrationNumber:
    def __init__(self, registration_number: str) -> None:
        self.__registration_number = self.__validate_registration_number(
            registration_number
        )

    def __validate_registration_number(self, registration_number: str) -> str:
        registration_number = re.sub(r"\s|\D", "", registration_number)
        if not registration_number.isdigit():
            raise ValueError("Only numeric values can be entered")

        if len(registration_number) == 11:
            registration_number = re.sub(
                r"(\d{3})(\d{3})(\d{3})(\d{2})",
                r"\1.\2.\3-\4",
                registration_number,
            )
        elif len(registration_number) == 14:
            registration_number = re.sub(
                r"(\d{2})(\d{3})(\d{3})(\d{4})(\d{2})",
                r"\1.\2.\3/\4-\5",
                registration_number,
            )
        else:
            raise ValueError("Registration number is not valid")
        return registration_number

    def get_value(self):
        return self.__registration_number
