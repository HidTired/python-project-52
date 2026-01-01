import pytest


@pytest.mark.django_db
class TestUser:
    def test_load_users(self, django_user_model):
        users = django_user_model.objects.all()
        assert len(users) == 3
