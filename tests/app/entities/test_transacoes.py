import pytest 
from src.app.entities.transaction import Transaction
from src.app.errors.entity_errors import ParamNotValidated
from src.app.enums.transaction_type_enum import TransactionTypeEnum


class Test_Transaction: 
    def test_transaction(self):
        transaction = Transaction(TransactionTypeEnum.DEPOSIT, 43, 4300, 1)
        assert transaction.type_transaction == TransactionTypeEnum.DEPOSIT
        assert transaction.value == 43   
        assert transaction.current_balance == 4300
        assert transaction.timestamp == 1
        
    def test_transaction_dict(self):
        transaction = Transaction(TransactionTypeEnum.DEPOSIT, 43, 4300, 1)
        assert transaction.to_dict() == {'type_transaction': 'DEPOSIT', 'value_transaction': 43, 'current_balance': 4300, 'time_stamp': 1}
    
    def test_transaction_type_is_none(self):
        with pytest.raises(ParamNotValidated):
            transaction = Transaction(None, 43, 4300, 1)
            
    def test_transaction_value_is_none(self):
        with pytest.raises(ParamNotValidated):
            transaction = Transaction(TransactionTypeEnum.DEPOSIT, None, 4300, 1)
            
    def test_transaction_current_balance_is_none(self):
        with pytest.raises(ParamNotValidated):
            transaction = Transaction(TransactionTypeEnum.DEPOSIT, 43, None, 1)
            
    def test_transaction_time_stamp_is_none(self):
        with pytest.raises(ParamNotValidated): 
            transaction = Transaction(TransactionTypeEnum.DEPOSIT, 43, 4300, None)
            
    def test_transaction_value_is_not_float(self):
        with pytest.raises(ParamNotValidated):
            transaction = Transaction(TransactionTypeEnum.DEPOSIT, "43string", 4300, 1)
            
    def test_transaction_current_balance_is_not_float(self):
        with pytest.raises(ParamNotValidated):
            transaction = Transaction(TransactionTypeEnum.DEPOSIT, 43, "43string", 1)
            
        