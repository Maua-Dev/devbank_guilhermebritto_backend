from typing import Tuple

class User:
    name: str
    agency: str
    account: str
    current_balance: float

    def __init__(self, name: str, agency: str, account: str, current_balance: float):
        validar_nome = self.validate_name(name)
        if validar_nome[0] == False:
            raise Exception("name", validar_nome[1])
        self.name = name

        validar_agencia = self.validate_agency(agency)
        if validar_agencia[0] == False:
            raise Exception("agency", validar_agencia[1])
        self.agency = agency
        
    @staticmethod
    def validate_name(name) -> Tuple[bool, str]:
        if name == None:
            return(False, "Insira um nome")
        
        if type(name) != str or len(name) < 3:
            return(False, "Insira um nome válido")
        
        return (True, "nome válido")
    
    @staticmethod
    def validate_agency(agency) -> Tuple[bool, str]:
        if agency == None:
            return(False, "Insira uma agência")
        
        if len(agency) !=4 or not agency.isdigit():
            raise Exception("A agência deve conter 4 dígitos!")

        return (True, "Agência válida")
    @staticmethod
    def validate_account():
        pass

    @staticmethod
    def validate_current_balance():
        pass


teste = User("oiiii", "4343", "aaaa", 1000)
print(teste)
