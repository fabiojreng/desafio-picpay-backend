import bcrypt


class Password:
    def __init__(self, password: str) -> None:
        self.value = password

    @staticmethod
    def create(password: str):
        password = password.replace(" ", "")
        if len(password) < 8:
            raise ValueError("Invalid password")
        hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
        return Password(hashed_password.decode("utf-8"))

    def validate(self, password: str) -> bool:
        return bcrypt.checkpw(password.encode("utf-8"), self.value.encode("utf-8"))

    def get_value(self) -> str:
        return self.value
