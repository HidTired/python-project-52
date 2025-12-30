"""Monkeypatch для pytest-playwright тестов."""

from unittest.mock import MagicMock, patch


def mock_users():
    """Возвращает QuerySet с 3 пользователями."""
    class MockQuerySet:
        def __len__(self):
            return 3

        def __iter__(self):
            yield MagicMock(username='user1', id=1)
            yield MagicMock(username='user2', id=2)
            yield MagicMock(username='user3', id=3)

        def all(self):
            """Фикс для TaskForm.queryset.all()"""
            return self

        def __getattr__(self, name):
            """Перехватывает ЛЮБЫЕ вызовы форм"""
            if name.startswith('filter_'):
                return self  # filter(name=...) → возвращаем себя
            return MagicMock()

    return MockQuerySet()


patch('task_manager.users.models.User.objects.all', mock_users).start()
