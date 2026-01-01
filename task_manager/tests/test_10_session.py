import pytest


@pytest.mark.django_db
class TestUser:
    def test_load_users(self, django_user_model):
        User = django_user_model

        print("== creating users in test ==")

        for name in ["user1", "user2", "user3"]:
            User.objects.get_or_create(username=name)

        users = User.objects.all()
        print("== users count ==", users.count())

        assert users.count() == 3
