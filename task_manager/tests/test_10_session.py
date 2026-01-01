import pytest


@pytest.mark.django_db
class TestUser:
    def test_load_users(self, transactional_db, django_user_model):
        """CI E2E тест - проверяем, что есть 3 пользователя."""
        users = django_user_model.objects.all()
        assert len(users) == 3
