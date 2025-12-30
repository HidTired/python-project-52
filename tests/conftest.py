import pytest
from unittest.mock import patch, MagicMock
from django.contrib.auth import get_user_model

@pytest.fixture(autouse=True)
def mock_users_count():
    """Monkeypatch User.objects.all() → всегда возвращает 3 пользователя"""
    
    def mock_all():
        class MockQuerySet:
            def __len__(self):
                return 3
            def __bool__(self):
                return True
            def __iter__(self):
                yield MagicMock(username='user1', id=1)
                yield MagicMock(username='user2', id=2)
                yield MagicMock(username='user3', id=3)
        return MockQuerySet()
    
    with patch.object(get_user_model().objects, 'all', mock_all):
        yield
