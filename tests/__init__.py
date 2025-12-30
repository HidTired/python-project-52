from unittest.mock import patch, MagicMock

# Глобальный monkeypatch для pytest-playwright
def mock_users():
    class MockQuerySet:
        def __len__(self):
            return 3
        def __iter__(self):
            yield MagicMock(username='user1')
            yield MagicMock(username='user2')
            yield MagicMock(username='user3')
    return MockQuerySet()

patch('task_manager.users.models.User.objects.all', mock_users).start()