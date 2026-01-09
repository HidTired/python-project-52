from django.contrib.auth import get_user_model
from django.test import TestCase

User = get_user_model()


class UserTestCase(TestCase):
    def setUp(self):
        self.admin = User.objects.create_superuser(
            username='admin',
            password='adminpass'
        )
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass',
            first_name='Test',
            last_name='User'
        )
        self.other_user = User.objects.create_user(
            username='otheruser',
            password='otherpass',
            first_name='Other',
            last_name='User'
        )

    def test_user_create_view(self):
        self.client.login(username='admin', password='adminpass')
        response = self.client.post('/users/create/', {
            'username': 'newuser2',
            'first_name': 'New',
            'last_name': 'User',
            'password1': 'pass123',
            'password2': 'pass123'
        })
        self.assertEqual(response.status_code, 302)  

    def test_user_list_view(self):
        self.client.login(username='admin', password='adminpass')
        response = self.client.get('/users/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'testuser')

    def test_admin_can_delete_user(self):
        self.client.login(username='admin', password='adminpass')
        response = self.client.post(f'/users/{self.other_user.id}/delete/', {})
        self.assertEqual(response.status_code, 302)
        self.assertFalse(User.objects.filter(id=self.other_user.id).exists())

    def test_cannot_delete_other_user(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(f'/users/{self.other_user.id}/delete/', {})
        self.assertEqual(response.status_code, 302) 
        self.assertEqual(User.objects.count(), 3)    
