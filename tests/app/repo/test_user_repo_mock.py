from ..entities.transaction import Transaction
from ..enums.transaction_type_enum import TransactionTypeEnum
from ..repo.user_repo_mock import UserRepositoryMock


class Test_UserRepositoryMock:

    def test_get_user(self):
        repo= UserRepositoryMock()

        user= repo.get_user(1)
        exceptUser = repo.users.get(1)

        assert user == exceptUser

    def test_get_user_not_found(self):
        repo= UserRepositoryMock()

        user= repo.get_user(id_user=10)

        assert user is None

    def test_current_balance_after_transaction_withdraw(self):
        repo= UserRepositoryMock()

        withdrawTransaction= Transaction(type=TransactionTypeEnum.withdraw, value=430.0, current_balance=4300.0, timestamp=123.4)
        balance_after_transaction= repo.current_balance_after_transaction(withdrawTransaction, id_user=1)

        assert balance_after_transaction == 3870.0

    def test_current_balance_after_transaction_deposit(self):
        repo= UserRepositoryMock()

        depositTransaction= Transaction(type=TransactionTypeEnum.deposit, value=430.0, current_balance=4300.0, timestamp=123.4)
        balance_after_transaction= repo.current_balance_after_transaction(depositTransaction, id_user=1)

        assert balance_after_transaction == 4730.0 