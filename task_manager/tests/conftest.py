import pytest
from django.contrib.auth import get_user_model


@pytest.fixture(autouse=True)
def create_test_users(django_user_model, django_db_blocker):
    """Создаёт user1, user2, user3 перед каждым тестом."""
    with django_db_blocker.unblock():
        User = get_user_model()
        for username in ["user1", "user2", "user3"]:
            User.objects.get_or_create(username=username)