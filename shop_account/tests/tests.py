from django.test import TestCase, SimpleTestCase, Client
from django.urls import reverse, resolve
from shop_account.views import login_view
from django.contrib.auth import get_user_model
import pytest

User = get_user_model()


class TestUrls(SimpleTestCase):
    def test_account_login_view_url(self):
        client = Client()
        url = reverse('login')
        response = client.get(url)
        self.assertEqual(resolve(url).func, login_view)
        self.assertTemplateUsed(response=response, template_name='account/login.html')
        self.assertEqual(response.status_code, 200)


class UserTesting(TestCase):
    def setUp(self):
        self.obj = User.objects.create_user(username='abc', password='abc123')

    def test_user_is_created(self):
        self.assertEqual(self.obj.username, 'abc', msg='checked')


def test_superuser(create_superuser):
    assert create_superuser.username == 'aabc'


def test_staff_user(create_staff_user):
    assert create_staff_user.username == 'aabc'


def test_factory_boy_superuser(factory_boy_superuser):
    assert factory_boy_superuser.username is not None
