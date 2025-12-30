from django.db import migrations

def create_test_users(apps, schema_editor):
    """Создаёт 3 пользователя БЕЗ паролей для CI тестов"""
    User = apps.get_model('users', 'User')
    
    # Создаём пользователей без паролей (для E2E теста достаточно username)
    User.objects.bulk_create([
        User(username='user1', first_name='John', last_name='Doe'),
        User(username='user2', first_name='Jane', last_name='Smith'),
        User(username='user3', first_name='Bob', last_name='Johnson'),
    ], ignore_conflicts=True)

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
