from src.app.entities.transaction import Transaction
from src.app.enums.transaction_type_enum import TransactionTypeEnum
from src.app.repo.transacoes_repo_mock import TransactionRepositoryMock

class Test_TransactionRepositoryMock:
    def test_get_all_transaction(self):
        repo=TransactionRepositoryMock()

        transactions= repo.get_all_transactions()
        expectTransactions= list(repo.transactions.values())

        assert expectTransactions == transactions

    def test_get_transaction(self):
        repo=TransactionRepositoryMock()

        transaction= repo.get_transaction(transaction_id=1)
        exceptTransaction= repo.transactions.get(1, None)

        assert exceptTransaction == transaction

    def test_get_transaction_not_found(self):
        repo= TransactionRepositoryMock()

        transaction= repo.get_transaction(transaction_id=10)

        assert transaction is None
