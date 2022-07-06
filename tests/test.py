from django.test import LiveServerTestCase
from selenium import webdriver
from django.urls import reverse
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from django.contrib.auth.models import User
import time
import pytest


def test_superuser(create_superuser):
    assert create_superuser.username == 'abc'


def test_staff_user(create_staff_user):
    assert create_staff_user.username == 'abc'

#
# class LiveTest(StaticLiveServerTestCase):
#     def setUp(self):
#         self.browser = webdriver.Chrome()
#
#     def tearDown(self):
#         self.browser.quit()
#
#
# def test_home_page(self):
#     self.browser.get(self.live_server_url)
#     self.assertEqual(self.browser.title, 'home page')
