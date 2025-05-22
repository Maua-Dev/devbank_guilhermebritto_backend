from typing import Dict, List, Optional
from ..entities.transaction import Transaction
from ..enums.transaction_type_enum import TransactionTypeEnum
from ..entities.user import User
from .user_repo_interface import InterfaceUserRepository

class UserRepositoryMock(InterfaceUserRepository):
    users: Dict[int, User]

    def __init__(self):
        self.users = {
            1: User("Guilherme 43", agency="4343", account="43434-3", current_balance=4300.0),
            2: User("nao sei", agency="0000", account="00043-0", current_balance=2000.0),
        }
    
    def get_user(self, id_user: int) -> Optional[User]:
        return self.users.get(id_user, None)
    
    
    def current_balance_after_transaction(self, transaction:Transaction, id_user: int) -> float:
        user= self.users.get(id_user, None)
        if transaction.type == TransactionTypeEnum.withdraw:
            user.current_balance -= transaction.value
        if transaction.type == TransactionTypeEnum.deposit:
            user.current_balance += transaction.value
        return user.current_balance