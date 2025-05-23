from enum import Enum
import os
from .errors.environment_errors import EnvironmentNotFound
from .repo.user_repo_interface import InterfaceUserRepository
from .repo.transacoes_repo_interface import InterfaceTransactionRepository
from .repo.user_repo_mock import UserRepositoryMock
from .repo.transacoes_repo_mock import TransactionRepositoryMock


class STAGE(Enum):
    DOTENV = "DOTENV"
    DEV = "DEV"
    PROD = "PROD"
    TEST = "TEST"

class Environments:
    """
    43
    """

    stage: STAGE

    def _configure_local(self):
        from dotenv import load_dotenv
        load_dotenv()
        os.environ["STAGE"] = os.environ.get("STAGE") or STAGE.TEST.value

    def load_envs(self):
        if "STAGE" not in os.environ or os.environ["STAGE"] == STAGE.DOTENV.value:
            self._configure_local()

        self.stage = STAGE[os.environ.get("STAGE")]

    @staticmethod
    def get_user_repo() -> InterfaceUserRepository:
        if Environments.getenvs().stage == STAGE.TEST:
            return UserRepositoryMock
        
        else:
            raise EnvironmentNotFound("STAGE")
        
    @staticmethod
    def get_transaction_repo() -> InterfaceTransactionRepository:
        if Environments.getenvs().stage == STAGE.TEST:
            return TransactionRepositoryMock
        
        else:
            raise EnvironmentNotFound("STAGE")
        

    @staticmethod
    def get_envs() -> "Environments":
        """
        Returns the Environments object. This method should be used to get the Environments object instead of instantiating it directly.
        :return: Environments (stage={self.stage})

        """
        envs = Environments()
        envs.load_envs()
        return envs
        
    def __repr__(self):
        return f"Environments(stage={self.stage})"