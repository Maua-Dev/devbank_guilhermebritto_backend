import pytest
from src.app.entities.user import User
from src.app.errors.entity_errors import ParamNotValidated

class Test_user:
    def Test_user(self):
        teste43 = User("gui43", "4343", "43434-4", 4300)
        assert teste43.name == "gui43"
        assert teste43.agency == "4343"
        assert teste43.account == "43434-4"
        assert teste43.current_balance == 4300

    def test_user_dict(self):
        teste43 = User("gui43", "4343", "43434-3", 4300)
        assert teste43.to_dict() == {'name': 'gui43', 'agency': "4343", 'account': "43434-3", 'current_balance': 4300}
    
    def test_user_name_is_none(self):
       with pytest.raises(ParamNotValidated):
          User(None, agency="4343", account="43434-3", current_balance=4300)

    def test_user_agency_is_none(self):
       with pytest.raises(ParamNotValidated):
          User(name="gui43", agency=None, account="43434-3", current_balance=4300)

    def test_user_account_is_none(self):
       with pytest.raises(ParamNotValidated):
          User(name="gui43", agency="4343", account=None, current_balance=4300)

    def test_user_current_balance_is_none(self):
       with pytest.raises(ParamNotValidated):
          User(name="gui43", agency="4343", account="43434-3", current_balance=None)

    def test_user_name_is_not_string(self):
       with pytest.raises(ParamNotValidated):
          User(name=4343, agency="4343", account="43434-3", current_balance=4300)

    def test_user_agency_is_not_str(self):
       with pytest.raises(ParamNotValidated):
          User(name="gui43", agency=4343, account="43434-3", current_balance=4300)

    def test_user_current_balance_is_not_float(self):
       with pytest.raises(ParamNotValidated):
          User(name="gui43", agency="4343", account="43434-3", current_balance="4300")

    def test_user_name_is_too_short(self):
         with pytest.raises(ParamNotValidated):
            User(name="gu", agency="4343", account="43434-3", current_balance=4300) 

    def test_user_account_is_not_valide(self): 
          with pytest.raises(ParamNotValidated):
               User(name="gui43", agency="4343", account="4343", current_balance=4300)    
       
    def test_uses_current_balance_is_negative(self):
         with pytest.raises(ParamNotValidated):
            User(name="gui43", agency="4343", account="43434-3", current_balance=-4300)