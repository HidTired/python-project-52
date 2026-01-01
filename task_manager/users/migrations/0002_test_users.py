from django.db import migrations


def create_test_users(apps, schema_editor):
    User = apps.get_model("users", "User")

    # На всякий случай подчистим
    User.objects.filter(username__in=["user1", "user2", "user3"]).delete()

    # Создаём ровно трёх пользователей
    User.objects.create(username="user1", password="123")
    User.objects.create(username="user2", password="123")
    User.objects.create(username="user3", password="123")


def delete_test_users(apps, schema_editor):
    User = apps.get_model("users", "User")
    User.objects.filter(username__in=["user1", "user2", "user3"]).delete()


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(create_test_users, delete_test_users),
    ]
