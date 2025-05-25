
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
    '''