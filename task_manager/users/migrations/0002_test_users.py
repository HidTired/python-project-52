from django.db import migrations
from django.contrib.auth.hashers import make_password

def create_test_users(apps, schema_editor):
    """Создаёт 3 пользователя для CI E2E тестов"""
    User = apps.get_model('users', 'User')
    
    # Создаём пользователей с паролями
    users = [
        User(username='user1', first_name='John', last_name='Doe'),
        User(username='user2', first_name='Jane', last_name='Smith'),
        User(username='user3', first_name='Bob', last_name='Johnson'),
    ]
    
    # Устанавливаем пароли после создания (bulk_create не работает с паролями)
    for user in users:
        user.set_password('testpass123')
        user.save()
    
    User.objects.bulk_create(users, ignore_conflicts=True)

def reverse_create_test_users(apps, schema_editor):
    """Удаляет тестовых пользователей"""
    User = apps.get_model('users', 'User')
    User.objects.filter(username__in=['user1', 'user2', 'user3']).delete()

class Migration(migrations.Migration):
    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_test_users, reverse_create_test_users),
    ]