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
from src.Application.UseCases.find_all_transactions import FindAllTransactionsUseCase
from src.Application.UseCases.find_transaction_by_id import FindTransactionByIdUseCase
from src.Application.UseCases.find_user_by_id import FindUserByIdUseCase
from src.Application.Decorator.autenticator_authorization import (
    AutenticatorAuthorizationDecorator,
)
from src.Infra.Gateway.authotization_gateway import AuthorizationGateway
from src.Infra.Http.request_client import RequestHttpClient


server = FlaskAdapter()
connection = ConnectionMySql()
db_user = UserRepositoryMySQL(connection)
db_transaction = TransactionRepositoryMySQL(connection)
http_client = RequestHttpClient()
authorization_gateway = AuthorizationGateway(http_client)
authorization_decorator = AutenticatorAuthorizationDecorator(authorization_gateway)

create_user = CreateUserUseCase(db_user)
deposit_amount = DepositAmountUseCase(db_user)
transaction = CreateTransactionUseCase(db_transaction, db_user, authorization_decorator)
find_all_transactions = FindAllTransactionsUseCase(db_transaction)
find_transaction_id = FindTransactionByIdUseCase(db_transaction)
find_user_id = FindUserByIdUseCase(db_user)

MainController(
    server,
    create_user,
    deposit_amount,
    transaction,
    find_all_transactions,
    find_transaction_id,
    find_user_id,
)
server.listen(3333)
