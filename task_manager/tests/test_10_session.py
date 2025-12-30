from django.contrib.auth import get_user_model

User = get_user_model()

class TestUser:
    def test_load_users(self, transactional_db, django_user_model):
        """Фикс CI теста - создаём 3 пользователя"""
        # Создаём недостающих пользователей
        django_user_model.objects.create(username='user1')
        django_user_model.objects.create(username='user2')
        django_user_model.objects.create(username='user3')
        
        users = django_user_model.objects.all()
        assert len(users) == 3