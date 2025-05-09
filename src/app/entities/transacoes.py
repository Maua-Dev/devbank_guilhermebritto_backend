from typing import Tuple
from ..errors.entity_errors import ParamNotValidated

class Transacoes:
    tipo_transacao: str
    value: float
    current_balance: float
    timestamp: float

    def __init__(self, tipo_transacao: str, value: float, current_balance: float, timestamp: float):
        validar_tipo = self.validate_tipo_transacao(tipo_transacao)
        if validar_tipo[0] == False:
            return ParamNotValidated ("tipo_transacao", validar_tipo[1])
        self.tipo_transacao = tipo_transacao

        validar_valor = self.validate_value(value)
        if validar_valor[0] == False:
            return ParamNotValidated("value", validar_valor[0])
        self.value = value

        validar_saldo = self.validate_current_balance(current_balance)
        if validar_saldo[0] == False:
            return ParamNotValidated("current_balance", validar_saldo[0])
        self.current_balance = current_balance

        validar_tempo = self.validate_timestamp(timestamp)
        if validar_tempo[0] == False:
            return ParamNotValidated("timestamp", validar_tempo[1])
        self.timestamp = timestamp

    @staticmethod
    def validate_tipo_transacao(tipo_transacao) -> Tuple[bool, str]:
        if tipo_transacao != "withdraw" or tipo_transacao != "deposit":
            return (False, "Tipo de transação inválida")

        if tipo_transacao == None:
            return (False, "Insira um tipo de transação")
        
        return (True, "Tipo de transação válido")
    
    @staticmethod
    def validate_value(value) -> Tuple[bool, str]:
        if value == None:
            return (False, "Insira um valor")
        
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
    
    def __repr__(self):
        return f"Transação(tipo={self.tipo_transacao}, valor={self.value}, saldo={self.current_balance}, tempo={self.timestamp})"