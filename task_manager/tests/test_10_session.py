import pytest


@pytest.fixture(autouse=True)
def ensure_test_users(django_user_model, django_db_blocker):
    with django_db_blocker.unblock():
        User = django_user_model
        for username in ["user1", "user2", "user3"]:
            User.objects.get_or_create(username=username)


@pytest.mark.django_db
class TestUser:
    def test_load_users(self, transactional_db, django_user_model):
        users = django_user_model.objects.all()
        assert len(users) == 3
