from app.entities.user import User
from app.entities.transacoes import Transacoes

class UserRepository:
    
    def __init__(self):
        self.users = {
            1: User(name="gui43", agency=4343, account=43434-3, current_balance=1000.4300)
        }

    def get_all_users(self):
        return self.users.values()
    
    def get_user(self, user_id: int):
        return self.users.get(user_id, None)