from typing import Tuple
import re
from ..errors.entity_errors import ParamNotValidated

class User:
    name: str
    agency: str
    account: str
    current_balance: float

    def __init__(self, name: str, agency: str, account: str, current_balance: float):
        validar_nome = self.validate_name(name)
        if validar_nome[0] == False:
            raise ParamNotValidated("name", validar_nome[1])
        self.name = name

        validar_agencia = self.validate_agency(agency)
        if validar_agencia[0] == False:
            raise ParamNotValidated("agency", validar_agencia[1])
        self.agency = agency
        
        validar_conta = self.validate_account(account)
        if validar_conta[0] == False:
            raise ParamNotValidated("Account", validar_conta[1])
        self.account = account
        
        validar_saldo = self.validate_current_balance(current_balance)
        if validar_saldo[0] == False:
            raise ParamNotValidated("Current Balance", validar_saldo[1])
        self.current_balance = current_balance
        

    @staticmethod
    def validate_name(name) -> Tuple[bool, str]:
        if name == None:
            return(False, "Insert a name")
        
        if type(name) != str or len(name) < 3:
            return(False, "Insert a valid name")
        
        return (True, "Valid name")
    
    @staticmethod
    def validate_agency(agency) -> Tuple[bool, str]:
        if agency == None:
            return(False, "Insert an agency")
        
        if agency != str:
            return(False, "Agency must be string")
        
        if len(agency) !=4 or not agency.isdigit():
            raise Exception("Agency must have 4 digits")

        return (True, "Valid Agency")
    
    @staticmethod
    def validate_account(account) -> Tuple[bool, str]:
        if account == None:
            return (False, "Insert an account following XXXXX-X")
        
        if len(account) != 7:
            return(False, "Invalid account, follow XXXXX-X")
        
        if account != re.match("^([0,9]{5}\-[0,9]{1}})$"):
            return (False, "Account does not follow XXXXX-X")

        return (True, "Valid account")


    @staticmethod
    def validate_current_balance(current_balance) -> Tuple[bool, str]:
        if current_balance == None:
            return (False, "Balance can't be null")
        
        if type(current_balance) != float:
            return (False, "Balance must be float")
        
        if current_balance < 0:
            return (False, "Balance can't be negative")
        
        return (True, "Valid balance")


