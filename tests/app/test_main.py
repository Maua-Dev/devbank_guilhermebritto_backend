
from fastapi.exceptions import HTTPException
import pytest
from src.app.entities.user import User
from src.app.entities.transaction import Transaction
from src.app.enums.transaction_type_enum import TransactionTypeEnum
from src.app.main import get_user
from src.app.main import get_history
from src.app.repo.user_repo_mock import UserRepositoryMock
from src.app.repo.transacoes_repo_mock import TransactionRepositoryMock
from src.app.errors.entity_errors import ParamNotValidated
from src.app.main import deposit_transaction
from src.app.main import withdraw_transaction

class TestMain:
    def test_get_user(self):
        response = get_user()
        expected_user = {
            'name': 'Guilherme 43',
            'agency': '4343',
            'account': '43434-3',
            'current_balance': 4300.0,
        }
        assert response == expected_user
'''
    def test_get_history(self):
        repo = TransactionRepositoryMock()
        response = get_history()
        expected_history = [
            {
                'type': 'deposit',
                'value': 4300.0,
                'current_balance': 443.0,
                'timestamp': 123.4
            },
            {
                'type': 'withdraw',
                'value': 430.0,
                'current_balance': 443.0,
                'timestamp': 123.4
            }
        ]
        assert response == expected_history
    

    def test_withdraw_transaction(self):
        request = {
            "2": 1,
            "5": 0,
            "10": 0,
            "20": 0,
            "50": 0,
            "100": 0,
            "200": 0
        }
        response = withdraw_transaction(request)
        expected_response = {
            'current_balance': 441.0,
            'timestamp': 123.4
        }
        assert response == expected_response

    def test_deposit_transaction(self):
        request = {
            "2": 0,
            "5": 0,
            "10": 0,
            "20": 0,
            "50": 0,
            "100": 0,
            "200": 1
        }
        response = deposit_transaction(request)
        expected_response = {
            'current_balance': 643.0,
            'timestamp': 123.4
        }
        assert response == expected_response
'''