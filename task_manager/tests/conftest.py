import pytest


@pytest.fixture(autouse=True)
def ensure_test_users(django_user_model, django_db_blocker):
    """Гарантирует, что в БД есть user1, user2, user3."""
    with django_db_blocker.unblock():
        User = django_user_model

        for name in ["user1", "user2", "user3"]:
            User.objects.get_or_create(username=name)
