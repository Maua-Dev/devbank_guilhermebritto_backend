import pytest
from src.app.entities.user import User
from src.app.errors.entity_errors import ParamNotValidated

class Test_user:
    def test_user(self):
        user= User("gui43", agency="4343", account="43434-3", current_balance=4300.0)

        assert user.name == "gui43"
        assert user.agency == "4343"
        assert user.account == "43434-3"
        assert user.current_balance == 4300.0

    def test_user_to_dict(self):
        user= User("gui43", agency="4343", account="43434-3", current_balance=4300.0)
        assert user.user_to_dict() == {
            "name": "gui43",
            "agency": "4343",
            "account": "43434-3",
            "current_balance": 4300.0
        }
      

    def test_user_name_is_none(self):
        with pytest.raises(ParamNotValidated):
            User(agency="4343", account="43434-3")

    def test_user_name_is_not_string(self):
        with pytest.raises(ParamNotValidated):
            User(name=1, agency="4343", account="43434-3")

    def test_user_name_is_digit(self):
        with pytest.raises(ParamNotValidated):
            User(name="4343", agency="4343", account="43434-3")

    def test_user_name_is_too_short(self):
        with pytest.raises(ParamNotValidated):
            User(name="g", agency="4343", account="43434-3")
    
    def test_user_agency_is_none(self):
        with pytest.raises(ParamNotValidated):
            User(name="gui43", account="43434-3")

    def test_user_agency_is_not_str(self):
        with pytest.raises(ParamNotValidated):
            User(name="gui43", agency=4343, account="43434-3")

    def test_user_agency_len_is_not_on_the_digit_model(self):
        with pytest.raises(ParamNotValidated):
            User(name="gui43",agency="43435", account="43434-3")

    def test_user_account_is_none(self):
        with pytest.raises(ParamNotValidated):
            User(name="gui43",agency="4343")
    
    def test_user_account_is_not_str(self):
        with pytest.raises(ParamNotValidated):
            User(name="gui43", agency="4343", account=434343)

    def test_user_account_is_not_on_the_digit_model(self):
        with pytest.raises(ParamNotValidated):
            User(name="gui43",agency="4343", account="434343")
    
    def test_current_balance_is_not_float(self):
        with pytest.raises(ParamNotValidated):
            User(name="gui43",agency="4343", account="43434-3", current_balance=4300)
    
    def test_current_balance_is_negative(self):
        with pytest.raises(ParamNotValidated):
            User(name="gui43",agency="4343", account="43434-3", current_balance=-4300.0)
    