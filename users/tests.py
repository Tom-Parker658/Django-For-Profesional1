from django.contrib.auth import get_user_model
from django.test import TestCase


class CustomUserTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='user1',
            email='user1@gmail.com',
            password='PapyrusGolden13',
        )
        self.assertEqual(user.username, 'user1')
        self.assertEqual(user.email, 'user1@gmail.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username='superuser1',
            email='superuser1@gmail.com',
            password='superPapyrusGolden13'
        )
        self.assertEqual(admin_user.username, 'superuser1')
        self.assertEqual(admin_user.email, 'superuser1@gmail.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
# Create your tests here.
