
import pytest

from task_manager.users.models import User


@pytest.fixture(autouse=True)
def mock_test_users(django_db_setup, django_db_blocker):
    """Monkeypatch для ВСЕХ тестов - создаём 3 пользователя"""
    with django_db_blocker.unblock():
        User.objects.all().delete()  # Очищаем
        User.objects.create(username='user1', password='123')
        User.objects.create(username='user2', password='123')
        User.objects.create(username='user3', password='123')


@pytest.fixture
def django_user_model():
    from django.contrib.auth import get_user_model
    return get_user_model()
