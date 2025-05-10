import pytest
from src.app.entities.user import User

class Test_user:
    def __init__(self):
        teste43 = User("gui43", "4343", "43434-4", 4300)
        assert teste43.name == "gui43"
        assert teste43.agency == "4343"
        assert teste43.account == "43434-4"
        assert teste43.current_balance == 4300

        