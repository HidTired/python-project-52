import pytest


@pytest.fixture(autouse=True)
def create_test_users(django_user_model, django_db_blocker):
    """Создаёт ровно 3 тестовых пользователя в БД без конфликтов username."""
    with django_db_blocker.unblock():
        User = django_user_model

        # сначала удаляем, чтобы не ловить UNIQUE
        User.objects.filter(username__in=["user1", "user2", "user3"]).delete()

        User.objects.create(username="user1", password="123")
        User.objects.create(username="user2", password="123")
        User.objects.create(username="user3", password="123")
