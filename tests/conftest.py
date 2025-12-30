import pytest
from django.core.management import call_command
from dotenv import load_dotenv

load_dotenv()


@pytest.fixture(scope='session')
def django_db_setup(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        call_command('migrate', '--noinput')


@pytest.fixture(autouse=True)
def create_test_users(django_user_model, django_db_blocker):
    """✅ Создаёт 3 пользователя напрямую в тестовой БД"""
    with django_db_blocker.unblock():
        User = django_user_model
        User.objects.create(username='user1', password='123')
        User.objects.create(username='user2', password='123')
        User.objects.create(username='user3', password='123')