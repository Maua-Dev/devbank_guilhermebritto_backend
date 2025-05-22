from src.app.entities import Environments
from fastapi import FastAPI, HTTPException
from mangum import Mangum
from src.app.repo.transacoes_repo_mock import TransactionRepositoryMock
from src.app.entities.transaction import Transaction
from src.app.repo.user_repo_mock import UserRepositoryMock
from src.app.errors.entity_errors import ParamNotValidated
from src.app.enums.item_type_enum import ItemTypeEnum
from src.app.entities.user import User

app = FastAPI()

use_id = 1

user_repo = Environments.get_user_repo()
transaction_repo = Environments.get_transaction_repo()

@app.get("/")
def get_user():
    user = user_repo.get_user(user_id = use_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    return {
        "user_id": use_id,
        "user": user.to_dict()
    }




handler = Mangum(app, lifespan="off")