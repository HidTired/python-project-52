import pytest

from task_manager.users.models import User


@pytest.fixture(autouse=True)
def create_test_users():
    """Создаёт 3 пользователей для КАЖДОГО теста"""
    User.objects.filter(username__in=['user1', 'user2', 'user3']).delete()
    User.objects.create(username='user1', password='123')
    User.objects.create(username='user2', password='123')
    User.objects.create(username='user3', password='123')