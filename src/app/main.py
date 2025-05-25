from .environments import Environments
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

UserRepositoryMock = Environments.get_user_repo()()
TransactionRepositoryMock = Environments.get_transaction_repo()()

@app.get("/")
def get_user():
    #user = User(get_user = UserRepositoryMock.get_user(id_user = use_id))
    user = UserRepositoryMock.get_user(id_user = use_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    return user.user_to_dict()


@app.get("/history")
def get_history():
    transactions = TransactionRepositoryMock.get_all_transactions()
    if not transactions:
        raise HTTPException(status_code=404, detail="Transactions not found")
    
    transaction_dict = {"transactions": []}
    for transaction in transactions:
        transaction_dict["transactions"].append(transaction.transactions_to_dict())

    return transactions


@app.post("/withdraw")
def withdraw_transaction(transaction: Transaction):
    pass

@app.post("/deposit")
def deposit_transaction(request: dict):
    total = 0
    transaction = TransactionRepositoryMock.get_transaction()
    user = UserRepositoryMock.get_user(id_user=use_id)
    dois = request.get("2")
    cinco = request.get("5")
    dez = request.get("10")
    vinte = request.get("20")
    cinquenta = request.get("50")
    cem = request.get("100")
    duzentos = request.get("200")
    

    total = dois * 2 + cinco * 5 + dez * 10 + vinte * 20 + cinquenta * 50 + cem * 100 + duzentos * 200
    if total < 0:
        raise HTTPException(status_code=400, detail="Transaction is negative")
    elif total > 2 * user.current_balance:
        raise HTTPException(status_code=400, detail="Transaction is greater than 2x the current balance")
    else:
        current_balance = UserRepositoryMock.current_balance_after_transaction(total=total, id_user=use_id)
        transaction = TransactionRepositoryMock.create_deposit_transaction(
            transaction=Transaction(
                type=ItemTypeEnum.deposit,
                value=total,
                transaction_id=transaction.id
            )
        )
        
    return {
        "current_balance": current_balance,
        "timestamp": transaction.timestamp
    }
    
handler = Mangum(app, lifespan="off")