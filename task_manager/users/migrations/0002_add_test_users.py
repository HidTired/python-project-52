from django.db import migrations
from django.utils.crypto import get_random_string


def create_test_users(apps, schema_editor):
    """Создаёт 3 тестовых пользователя с безопасными паролями"""
    user_model = apps.get_model('users', 'User')

    def generate_secure_password():
        chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*'
        return get_random_string(16, chars) + '2026!'
    
    test_users_data = [
        {
            'username': 'user1',
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'user1@example.com',
            'password': generate_secure_password(),
        },
        {
            'username': 'user2',
            'first_name': 'Jane',
            'last_name': 'Smith',
            'email': 'user2@example.com',
            'password': generate_secure_password(),
        },
        {
            'username': 'user3',
            'first_name': 'Bob',
            'last_name': 'Johnson',
            'email': 'user3@example.com',
            'password': generate_secure_password(),
        },
    ]
    
    for user_data in test_users_data:
        if not user_model.objects.filter(username=user_data['username']).exists():
            user_model.objects.create_user(
                username=user_data['username'],
                first_name=user_data['first_name'],
                last_name=user_data['last_name'],
                email=user_data['email'],
                password=user_data['password'],
                is_active=True,
                is_staff=False,
                is_superuser=False,
            )
            print(f" Создан тестовый пользователь: {user_data['username']}")
            print(f"   Пароль: {user_data['password']}")


def remove_test_users(apps, schema_editor):
    """Удаляет тестовых пользователей (для отката миграции)"""
    user_model = apps.get_model('users', 'User')
    usernames = ['user1', 'user2', 'user3']
    user_model.objects.filter(username__in=usernames).delete()


class Migration(migrations.Migration):
    dependencies = [
        ('users', '0001_initial'),
    ]
    
    operations = [
        migrations.RunPython(
            create_test_users,
            reverse_code=remove_test_users
        ),
    ]
