from app.entities import Environments
from fastapi import FastAPI, HTTPException
from mangum import Mangum
from .repo.transacoes_repo_mock import TransactionRepositoryMock
from .entities.transaction import Transaction
from .repo.user_repo_mock import UserRepositoryMock
from .errors.entity_errors import ParamNotValidated
from .enums.item_type_enum import ItemTypeEnum
from .entities.user import User

app = FastAPI()

use_id = 1

UserRepositoryMock = Environments.get_user_repo()
TransactionRepositoryMock = Environments.get_transaction_repo()

@app.get("/")
def get_user():
    user = UserRepositoryMock.get_user(user_id = use_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    return {
        "user_id": use_id,
        "user": user.user_to_dict()
    }



handler = Mangum(app, lifespan="off")