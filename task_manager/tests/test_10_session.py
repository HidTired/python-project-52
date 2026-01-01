import pytest


@pytest.mark.django_db
class TestUser:
    def test_load_users(self, django_user_model):
        User = django_user_model

        print("=== TEST_10_SESSION STARTED ===")

        # Создаём тестовых пользователей
        for name in ["user1", "user2", "user3"]:
            u, created = User.objects.get_or_create(username=name)
            print("created:", name, "->", created)

        print("=== QUERY USERS ===")
        print("count():", User.objects.count())
        print("all():", list(User.objects.values_list("username", flat=True)))

        assert User.objects.count() == 3
