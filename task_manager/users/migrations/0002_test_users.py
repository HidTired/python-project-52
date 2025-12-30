from django.db import migrations

def create_test_users(apps, schema_editor):
    """Создаёт 3 пользователя БЕЗОШИБОЧНО"""
    User = apps.get_model('users', 'User')
    
    # ✅ 3 пользователя с правильными паролями
    users_data = [
        {'username': 'user1', 'password': '123'},
        {'username': 'user2', 'password': '123'},
        {'username': 'user3', 'password': '123'},
    ]
    
    for data in users_data:
        user, created = User.objects.get_or_create(
            username=data['username'],
            defaults={'password': data['password']}
        )
        if not created:
            # ✅ Обновляем пароль если пользователь уже существует
            user.set_password(data['password'])
            user.save()

def delete_test_users(apps, schema_editor):
    User = apps.get_model('users', 'User')
    User.objects.filter(username__in=['user1', 'user2', 'user3']).delete()

class Migration(migrations.Migration):
    dependencies = [('users', '0001_initial')]
    
    operations = [
        migrations.RunPython(create_test_users, delete_test_users),
    ]
