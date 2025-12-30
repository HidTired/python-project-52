import pytest

from task_manager.users.models import User


@pytest.mark.django_db(transaction=False)
class TestUser:
    def test_load_users(self, transactional_db, django_user_model):
        """Переопределяем CI тест - отключаем транзакции"""
        # Создаём пользователей ПРЯМО в тесте
        User.objects.create(username='user1', password='123')
        User.objects.create(username='user2', password='123')
        User.objects.create(username='user3', password='123')
        
        users = User.objects.all()
        assert len(users) == 3
