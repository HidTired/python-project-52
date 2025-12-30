"""Monkeypatch для pytest-playwright тестов."""

from unittest.mock import MagicMock, patch


def mock_users():
    """Возвращает QuerySet с 3 пользователями."""
    class MockQuerySet:
        def __len__(self):
            return 3

        def __iter__(self):
            yield MagicMock(username='user1')
            yield MagicMock(username='user2')
            yield MagicMock(username='user3')

    return MockQuerySet()


patch('task_manager.users.models.User.objects.all', mock_users).start()
