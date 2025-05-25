from typing import Dict, List, Optional
from ..entities.transaction import Transaction
from ..enums.transaction_type_enum import TransactionTypeEnum
from ..repo.transacoes_repo_interface import InterfaceTransactionRepository
from ..repo.user_repo_mock import UserRepositoryMock
from ..entities.user import User

class TransactionRepositoryMock(InterfaceTransactionRepository):
    transactions: Dict[int, Transaction]

    def __init__(self):
        self.transactions = {
            1: Transaction(type=TransactionTypeEnum.deposit, value=4300.0, current_balance=443.0, timestamp=123.4),

            2: Transaction(type=TransactionTypeEnum.withdraw, value=430.0, current_balance=443.0, timestamp=123.4)
        }
    
    def get_all_transactions(self) -> List[Transaction]:
        return list(self.transactions.values())
    
    def get_transaction(self, transaction_id:int) -> Optional[Transaction]:
        return self.transactions.get(transaction_id, None)
    
    def create_withdraw_transaction(self, transaction:Transaction) -> Optional[Transaction]:
        if transaction.type != TransactionTypeEnum.withdraw:
            return None
        self.transactions[len(self.transactions) +1]= transaction
        return transaction

    def create_deposit_transaction(self, transaction: Transaction) -> Optional[Transaction]:
        if transaction.type != TransactionTypeEnum.deposit:
            return None
        self.transactions[len(self.transactions) + 1]= transaction
        return transaction
    