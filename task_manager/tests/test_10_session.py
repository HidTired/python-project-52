import pytest


@pytest.mark.django_db
class TestUser:
    def test_load_users(self, django_user_model):
        User = django_user_model

        # ЯВНО создаю тестовых пользователей в тестовой БД
        for name in ["user1", "user2", "user3"]:
            User.objects.get_or_create(username=name)

        users = User.objects.all()
        assert len(users) == 3
