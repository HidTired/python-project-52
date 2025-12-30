from unittest.mock import MagicMock

import pytest
from django.contrib.auth import get_user_model


@pytest.fixture(autouse=True)
def mock_users_count(monkeypatch):
    """Monkeypatch для ВСЕХ тестов — возвращаем 3 пользователя"""
    User = get_user_model()
    
    def mock_all(self):
        class MockQuerySet:
            def __len__(self):
                return 3

            def __iter__(self):
                yield MagicMock(username='user1')
                yield MagicMock(username='user2')
                yield MagicMock(username='user3')
        return MockQuerySet()
    
    monkeypatch.setattr(User.objects, 'all', mock_all)
