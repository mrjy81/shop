from django.test import LiveServerTestCase
from selenium import webdriver
from django.urls import reverse, resolve
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from django.conf import settings
from django.contrib.auth import get_user_model
import time
import pytest
from django_seed import Seed
from shop_products.models import Products
from shop_products_category.models import ProductCategory
from django.test import RequestFactory

User = get_user_model()

seeder = Seed.seeder()


@pytest.mark.usefixtures('chrome_setup')
class LiveTest(LiveServerTestCase):
    @pytest.mark.skip
    def test_home_page(self):
        self.browser.get(self.live_server_url + '/admin')
        time.sleep(5)
        # assert 'home page' in self.browser.title


class AdminLiveTest(StaticLiveServerTestCase):
    # fixtures = ['fixtures/user.json', 'fixtures/products.json', 'fixtures/category.json']
    fixtures = ['fixtures/user.json']

    def setUp(self):
        self.browser = webdriver.Chrome()
        seeder.add_entity(ProductCategory, 5)
        seeder.add_entity(Products, 60)
        inserted_pks = seeder.execute()

    def tearDown(self):
        self.browser.quit()

    @pytest.mark.skip
    def test_login(self):
        self.browser.get('%s%s' % (self.live_server_url, '/admin'))
        username_input = self.browser.find_element(by=By.NAME, value="username")
        username_input.send_keys('abc')
        password_input = self.browser.find_element(by=By.NAME, value="password")
        password_input.send_keys(123)
        self.browser.find_element(by=By.XPATH, value='//input[@value="ورود"]').click()
        assert 'مدیریت وب‌گاه | مدیریت وب‌گاه Django' in self.browser.title

    def test_products(self):
        self.browser.get(self.live_server_url + '/products')

    @pytest.mark.cart
    def test_add_to_cart(self):
        self.browser.get(self.live_server_url + '/products')
        element = self.browser.find_element(by=By.CLASS_NAME, value='add-to-cart')
        element.send_keys(Keys.RETURN)
        element2 = self.browser.find_element(by=By.ID, value='add-to-cart')
        time.sleep(1)
        element2.send_keys(Keys.RETURN)
        self.browser.get(self.live_server_url + '/cart-orders/cart')
        time.sleep(50)

    def test_delete_from_cart(self):
        self.browser.get(self.live_server_url + '/cart-orders/cart')
        delete_btn = self.browser.find_element(by=By.CLASS_NAME, value='cart_quantity_delete')
        delete_btn.send_keys(Keys.RETURN)
        time.sleep(1)

    def test_home_page_login(self):
        self.browser.get(self.live_server_url + '/account/login')
        time.sleep(1)
        username_input = self.browser.find_element(by=By.NAME, value="username")
        username_input.send_keys('abc')
        password_input = self.browser.find_element(by=By.NAME, value="password")
        password_input.send_keys(123)
        self.browser.find_element(by=By.XPATH, value='//input[@value="ورود"]').click()
        time.sleep(1)
