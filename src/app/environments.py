from enum import Enum
import os
from .errors.environment_errors import EnvironmentNotFound
from .repo.user_repo_interface import IUserRepository
from .repo.transaction_repo_interface import ITransactionRepository
from .repo.user_repo_mock import UserRepositoryMock
from .repo.transaction_repo_mock import TransactionRepositoryMock


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
    def get_user_repo() -> IUserRepository:
        if Environments.getenvs().stage == STAGE.TEST:
            return UserRepositoryMock
        
        else:
            raise EnvironmentNotFound("STAGE")
        
    @staticmethod
    def get_transaction_repo() -> ITransactionRepository:
        if Environments.getenvs().stage == STAGE.TEST:
            return TransactionRepositoryMock
        
        else:
            raise EnvironmentNotFound("STAGE")
        
    def __repr__(self):
        return self.__dict__