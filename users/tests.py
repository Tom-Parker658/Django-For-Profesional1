from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse, resolve 

from .forms import CustomUserCreationForm
from .views import SignupPageView

# Test for user creation in the admin panel
class CustomUserTests(TestCase):
    # Test for a normal user created
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
    # Test for a superuser created
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

#Test for the signup page process
class SignupPageTest(TestCase):

    def setUp(self):
        url = reverse('signup')
        self.response = self.client.get(url)
    
    def test_signup_template(self):
        self.assertEqual(self.response.status_code,200)
        self.assertTemplateUsed(self.response, 'signup.html') 
        self.assertContains(self.response, 'Sign Up')
        self.assertNotContains(self.response, 'bla bla')

    def test_sigup_form(self):
        form = self.response.context.get('form')
        self.assertIsInstance(form, CustomUserCreationForm)
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_signup_view(self):
        view = resolve('/accounts/signup/')
        self.assertEqual(
            view.func.__name__,
            SignupPageView.as_view().__name__
        )
# Create your tests here.
