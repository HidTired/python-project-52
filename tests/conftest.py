from unittest.mock import MagicMock, patch

import pytest


@pytest.fixture(scope="session", autouse=True)
def django_test_setup(monkeypatch):
    """Monkeypatch ПОСЛЕ Django setup"""
    
    def mock_user_count():
        class MockQuerySet:
            def __len__(self):
                return 3

            def __iter__(self):
                for i in range(3):
                    yield MagicMock(username=f'user{i + 1}', id=i + 1)

            def exists(self):
                return True
        return MockQuerySet()
    
    # ✅ Monkeypatch конкретно task_manager.users.models.User
    with patch('task_manager.users.models.User.objects.all', mock_user_count):
        yield
