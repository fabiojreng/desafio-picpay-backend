import os, sys


sys.path.insert(0, os.path.abspath(os.curdir))

from src.Application.UseCases.create_transaction import CreateTransactionUseCase
from src.Application.UseCases.deposit_amount import DepositAmountUseCase
from src.Application.UseCases.create_user import CreateUserUseCase
from src.Infra.DataBase.connection_mysql import ConnectionMySql
from src.Infra.Http.flask_adapter import FlaskAdapter
from src.Infra.Repository.MySQL.user_repository_mysql import UserRepositoryMySQL
from src.Infra.Controller.main_controller import MainController
from src.Infra.Repository.MySQL.transaction_repository_mysql import (
    TransactionRepositoryMySQL,
)
from src.Application.UseCases.find_all_transactions import FindAllTransactions

server = FlaskAdapter()
connection = ConnectionMySql()
db_user = UserRepositoryMySQL(connection)
db_transaction = TransactionRepositoryMySQL(connection)

create_user = CreateUserUseCase(db_user)
deposit_amount = DepositAmountUseCase(db_user)
transaction = CreateTransactionUseCase(db_transaction, db_user)
find_all_transactions = FindAllTransactions(db_transaction)

MainController(server, create_user, deposit_amount, transaction, find_all_transactions)
server.listen(3333)
