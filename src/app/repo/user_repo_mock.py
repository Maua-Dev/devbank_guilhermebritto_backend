from ..entities.user import User
from typing import Dict, Optional, List
class User_repo_mock:

    def __init__(self):
        users = Dict[int, User]
        self.users = {
        1: User(name="gui43", agency=4343, account=43434-3, current_balance=4300),
        2: User(name="teste43", agency=4300, account="00000-0", current_balance=1000)
    }
        
    def get_all_users(self):
        return self.users.values()
    
    def get_user(self, user_id: int):
        return self.users.get(user_id, None)        
    
    def get_user_balance(self, user: User):
        return user.current_balance    
    
    def get_user_name(self, user: User):
        return user.name
    
    def get_user_agency(self, user: User):
        return user.agency  
    
    def get_user_account(self, user: User):
        return user.account

