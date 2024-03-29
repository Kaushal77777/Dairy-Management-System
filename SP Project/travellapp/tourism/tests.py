from django.test import TestCase
from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
import time

class TestProjectListPage(StaticLiveServerTestCase):
	def setUp(self):
		self.browser = webdriver.Chrome('chromedriver.exe')
		#self.browser = webdriver.Firefox()

	def tearDown(self):
		self.browser.close()

	def login_test(self):
		self.browser.get('http://127.0.0.1:8000/')
		self.browser.maximize_window()

		time.sleep(1)
		link = self.browser.find_element_by_link_text('Login')
		link.click()

		self.browser.find_element_by_name("username").send_keys("d123")
		time.sleep(1)
		self.browser.find_element_by_name("password").send_keys("123")
		time.sleep(1)
		self.browser.find_element_by_name("login").click()
		time.sleep(5)

	def register_test(self):
		self.browser.get('http://127.0.0.1:8000/')
		self.browser.maximize_window()

		time.sleep(1)
		link = self.browser.find_element_by_link_text('Register')
		link.click()

		self.browser.find_element_by_name("first_name").send_keys("Dhruvit")
		time.sleep(1)
		self.browser.find_element_by_name("last_name").send_keys("Ramani")
		time.sleep(1)
		self.browser.find_element_by_name("username").send_keys("d123")
		time.sleep(1)
		self.browser.find_element_by_name("email").send_keys("d@gmail.com")
		time.sleep(1)
		self.browser.find_element_by_name("password1").send_keys("123")
		time.sleep(1)
		self.browser.find_element_by_name("password2").send_keys("123")
		time.sleep(1)
		self.browser.find_element_by_name("register").click()
		time.sleep(5)




