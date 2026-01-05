import pytest


@pytest.mark.django_db
class TestUser:
    def test_load_users(self, django_user_model):
        User = django_user_model
        print("=== TEST_10_SESSION STARTED ===")

        # Создаём пользователей
        for name in ["user1", "user2", "user3"]:
            User.objects.create(username=name, password='password123') 
        
        print("=== QUERY USERS ===")
        users = User.objects.all()
        print(f"Found users: {list(users.values_list('username', flat=True))}")
        
        assert len(users) == 3
