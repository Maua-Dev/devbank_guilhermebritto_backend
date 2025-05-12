from ..entities.user import User
from ..errors.entity_errors import ParamNotValidated
class User_repo_mock:

    def __init__(self):
        self.users = {
        1: User(name="gui43", agency=4343, account=43434-3, current_balance=4300)
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