from django.db import migrations

def create_test_users(apps, schema_editor):
    User = apps.get_model('users', 'User')
    # ✅ update_or_create — НЕ падает при дубликатах!
    User.objects.update_or_create(username='user1', defaults={'password': '123'})
    User.objects.update_or_create(username='user2', defaults={'password': '123'})
    User.objects.update_or_create(username='user3', defaults={'password': '123'})

def delete_test_users(apps, schema_editor):
    User = apps.get_model('users', 'User')
    User.objects.filter(username__in=['user1', 'user2', 'user3']).delete()

class Migration(migrations.Migration):
    dependencies = [('users', '0001_initial')]
    
    operations = [
        migrations.RunPython(create_test_users, delete_test_users),
    ]
