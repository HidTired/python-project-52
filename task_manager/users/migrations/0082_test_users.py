from django.db import migrations
from django.contrib.auth.hashers import make_password

def create_test_users(apps, schema_editor):
    """Создаёт 3 пользователя для E2E тестов"""
    User = apps.get_model('users', 'User')
    User.objects.bulk_create([
        User(username='user1', password=make_password('pass')),
        User(username='user2', password=make_password('pass')),
        User(username='user3', password=make_password('pass')),
    ], ignore_conflicts=True)

class Migration(migrations.Migration):
    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_test_users),
    ]