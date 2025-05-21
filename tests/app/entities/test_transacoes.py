import pytest
from src.app.errors.entity_errors import ParamNotValidated
from src.app.entities.transaction import Transaction
from src.app.enums.transaction_type_enum import TransactionTypeEnum


class Test_transaction:
    def test_transaction(self):
        transaction = Transaction(type=TransactionTypeEnum.deposit, value=430.0, current_balance=4300.0, timestamp=123.4)
        assert transaction.type == TransactionTypeEnum.deposit
        assert transaction.value == 430.0
        assert transaction.current_balance == 4300.0
    
    def test_type_is_none(self):
        with pytest.raises(ParamNotValidated):
            Transaction(value=430, current_balance=4300.0, timestamp=123.4)

    def test_type_is_not_enum(self):
        with pytest.raises(ParamNotValidated):
            Transaction(type="deposit",value=430, current_balance=4300.0, timestamp=123.4)

    def test_value_is_none(self):
        with pytest.raises(ParamNotValidated):
            Transaction(type=TransactionTypeEnum.deposit, current_balance=4300.0, timestamp=123.4)
    
    def test_value_is_not_float(self):
        with pytest.raises(ParamNotValidated):
            Transaction(type=TransactionTypeEnum.deposit, value=200, current_balance=4300.0, timestamp=123.4)
    
    def test_value_is_negative(self):
        with pytest.raises(ParamNotValidated):
            Transaction(type=TransactionTypeEnum.deposit, value=-430, current_balance=4300.0, timestamp=123.4)

    def test_current_balance_is_none(self):
        with pytest.raises(ParamNotValidated):
            Transaction(type=TransactionTypeEnum.deposit, value=430, timestamp=123.4)
    
    def test_current_balance_is_not_float(self):
        with pytest.raises(ParamNotValidated):
            Transaction(type=TransactionTypeEnum.deposit, value=430, current_balance=4300, timestamp=123.4)
    
    def test_current_balance_is_negative(self):
        with pytest.raises(ParamNotValidated):
            Transaction(type=TransactionTypeEnum.deposit, value=430, current_balance=-4300.0, timestamp=123.4)

    def test_timestamp_is_none(self):
        with pytest.raises(ParamNotValidated):
            Transaction(type=TransactionTypeEnum.deposit, value=430, current_balance=4300.0)
    
    def test_timestamp_is_not_float(self):
        with pytest.raises(ParamNotValidated):
            Transaction(type=TransactionTypeEnum.deposit, value=430, current_balance=4300.0, timestamp=123.4)

    def test_timestamp_is_negative(self):
        with pytest.raises(ParamNotValidated):
            Transaction(type=TransactionTypeEnum.deposit, value=430, current_balance=4300.0, timestamp=-123.4)

    