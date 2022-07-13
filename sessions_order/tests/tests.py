from django.test import TestCase, LiveServerTestCase
from selenium import webdriver
from django.urls import reverse
from selenium.webdriver.common.by import By


# class TestSessionCart(LiveServerTestCase):
#     def setUp(self):
#         self.browser = webdriver.Chrome()
#
#     def tearDown(self):
#         self.browser.quit()
#
#     def test_add_to_cart(self):
#         self.browser.get(self.live_server_url + '/products')
#         element = self.browser.find_element(by=By.CLASS_NAME, value='add-to-cart')
#         print(element)

#
