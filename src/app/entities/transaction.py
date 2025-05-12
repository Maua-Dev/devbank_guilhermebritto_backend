from typing import Tuple
from ..errors.entity_errors import ParamNotValidated
from ..enums.transaction_type_enum import TransactionTypeEnum

class Transaction:
    type_transaction : TransactionTypeEnum 
    value: float
    current_balance: float
    timestamp: float

    def __init__(self, type_transaction: TransactionTypeEnum, value: float, current_balance: float, timestamp: float):
        validar_tipo = self.validate_type_transaction(type_transaction)
        if validar_tipo[0] == False:
            raise ParamNotValidated ("type_transaction", validar_tipo[1])
        self.type_transaction = type_transaction

        validar_valor = self.validate_value(value)
        if validar_valor[0] == False:
            raise ParamNotValidated("value", validar_valor[0])
        self.value = value

        validar_saldo = self.validate_current_balance(current_balance)
        if validar_saldo[0] == False:
            raise ParamNotValidated("current_balance", validar_saldo[0])
        self.current_balance = current_balance

        validar_tempo = self.validate_timestamp(timestamp)
        if validar_tempo[0] == False:
            raise ParamNotValidated("timestamp", validar_tempo[1])
        self.timestamp = timestamp

    @staticmethod
    def validate_type_transaction(type_transaction: TransactionTypeEnum) -> Tuple[bool,str]:
        if type_transaction is None:
            return (False, "Type is required")
        
        if type(type_transaction) != TransactionTypeEnum:
            return (False, "Type must be a TransactionTypeEnum")
        
        return (True, "Validation OK")
    
    @staticmethod
    def validate_value(value) -> Tuple[bool, str]:
        if value == None:
            return (False, "Insira um valor")
        
        if value != float:
            return (False, "Value must be float")
        
        if value < 0:
            return (False, "Valor não pode ser menor que 0")
        
        return (True, "Valor válido")

    @staticmethod
    def validate_current_balance(current_balance) -> Tuple[bool, str]:
        if current_balance == None:
            return (False, "Saldo não pode ser null")
        
        if type(current_balance) != float:
            return (False, "Saldo tem que ser do tipo float")
        
        if current_balance < 0:
            return (False, "Saldo não pode ser menor que 0")
        
        return (True, "Saldo válido")

    @staticmethod
    def validate_timestamp(timestamp) -> Tuple[bool, str]:
        if timestamp == None:
            return (False, "Tempo de transação inválido")
        
        if type(timestamp) != float:
            return (False, "Tempo tem que ser float")
        
        if timestamp < 0:
            return (False, "Tempo não pode ser negativo")
        
        return (True, "Tempo válido")
    