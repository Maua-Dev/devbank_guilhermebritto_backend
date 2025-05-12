from ..enums.transaction_type_enum import TransactionTypeEnum
from ..entities.transaction import Transaction

from typing import Dict, Optional, List 


class Transaction_repo_mock:
    transaction: Dict[int, Transaction]
    
    def __init__(self):
        self.transaction = {
            1: Transaction(tipo_transacao=TransactionTypeEnum.DEPOSIT, value=100.0, current_balance=4300, timestamp=1),
            2: Transaction(tipo_transacao=TransactionTypeEnum.WITHDRAWAL, value=50.0, current_balance=1000, timestamp=1),
        }
        
    def get_all_transactions(self) -> List[Transaction]:
        return self.transaction.values()
    
    def get_transaction(self, transaction_id: int) -> Optional[Transaction]:
        return self.transaction.get(transaction_id, None)
    
    def current_balance_after_transaction(self, transaction: Transaction) -> float:
        if transaction.type_transaction == TransactionTypeEnum.WITHDRAWAL:
            transaction.current_balance -= transaction.value_transaction
        elif transaction.type_transaction == TransactionTypeEnum.DEPOSIT:
            transaction.current_balance += transaction.value_transaction
        else:
            raise ValueError("Transaction type is invalid")
        return transaction.current_balance
     
     
    
    

    