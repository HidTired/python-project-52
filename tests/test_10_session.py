import pytest


@pytest.mark.django_db
class TestUser:
    def test_load_users(self, transactional_db, django_user_model):
        django_user_model.objects.create(username='user1')
        django_user_model.objects.create(username='user2')
        django_user_model.objects.create(username='user3')
        
        users = django_user_model.objects.all()
        assert len(users) == 3