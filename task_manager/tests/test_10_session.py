import pytest


@pytest.mark.django_db
class TestUser:
    def test_load_users(self, transactional_db):
        """CI тест - создаём пользователей ПЕРЕД проверкой"""
        from django.contrib.auth import get_user_model
        
        User = get_user_model()
        User.objects.create(username='user1')
        User.objects.create(username='user2')
        User.objects.create(username='user3')
        
        users = User.objects.all()
        assert len(users) == 3
