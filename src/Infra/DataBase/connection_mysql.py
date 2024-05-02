from src.Infra.DataBase.interface_connection import ConnectionInterface
import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()


class ConnectionMySql(ConnectionInterface):

    def connect(self) -> None:
        self.connection = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME"),
        )

    def query(self, statement: str, params: list = None):
        cursor = self.connection.cursor()

        cursor.execute(statement, params)

        if statement.strip().split(maxsplit=1)[0].upper() == "SELECT":
            result = cursor.fetchall()
        else:
            result = self.connection.commit()

        cursor.close()
        return result

    def close(self) -> None:
        self.connection.close()
