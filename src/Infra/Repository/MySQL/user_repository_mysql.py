from src.Domain.Entities.user import User
from src.Domain.Repository.user_repository import UserRepositoryInterface
from src.Infra.DataBase.connection_mysql import ConnectionMySql


class UserRepositoryMySQL(UserRepositoryInterface):
    def __init__(self, mysql: ConnectionMySql):
        self.__mysql = mysql

    def save_user(self, user: dict) -> None:
        self.__mysql.connect()
        self.__mysql.query(
            "INSERT INTO users (id, name, email, registration_number, user_type, password, amount) VALUES (%s, %s, %s, %s, %s, %s, %s)",
            [
                user["id"],
                user["name"],
                user["email"],
                user["registration_number"],
                user["user_type"],
                user["password"],
                user["amount"],
            ],
        )
        self.__mysql.close()

    def find_by_registration_number(self, registration: str) -> User:
        self.__mysql.connect()
        user = self.__mysql.query(
            "SELECT * FROM users WHERE registration_number = %s", [registration]
        )

        if not user:
            return None
        (
            user_id,
            user_name,
            user_email,
            user_registration_number,
            user_type,
            user_password,
            user_amount,
        ) = user[0]

        output = User.restore(
            user_id,
            user_name,
            user_email,
            user_registration_number,
            user_password,
            float(user_amount),
            user_type,
        )

        self.__mysql.close()
        return output

    def find_by_email(self, email: str) -> User:
        self.__mysql.connect()
        user = self.__mysql.query("SELECT * FROM users WHERE email = %s", [email])
        if not user:
            return None
        (
            user_id,
            user_name,
            user_email,
            user_registration_number,
            user_type,
            user_password,
            user_amount,
        ) = user[0]
        output = User.restore(
            user_id,
            user_name,
            user_email,
            user_registration_number,
            user_password,
            user_amount,
            user_type,
        ).to_dict()
        self.__mysql.close()
        return output

    def update_amount(self, value: float, registration_number: str) -> None:
        self.__mysql.connect()
        self.__mysql.query(
            "UPDATE users SET amount = %s WHERE registration_number = %s",
            [value, registration_number],
        )
        self.__mysql.close()

    def find_by_id(self, id: str) -> User:
        self.__mysql.connect()
        user = self.__mysql.query("SELECT * FROM users WHERE id = %s", [id])
        if not user:
            return None
        (
            user_id,
            user_name,
            user_email,
            user_registration_number,
            user_type,
            user_password,
            user_amount,
        ) = user[0]

        output = User.restore(
            user_id,
            user_name,
            user_email,
            user_registration_number,
            user_password,
            float(user_amount),
            user_type,
        )
        self.__mysql.close()
        return output
