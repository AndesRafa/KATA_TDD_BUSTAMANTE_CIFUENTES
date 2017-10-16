from django.test import TestCase
from selenium import webdriver

# Create your tests here.
class Test(TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome("C:\\Users\\JUAN CIFUENTES\\chromedriver.exe")
        self.browser.implicitly_wait(2)
    def tearDown(self):
        self.browser.quit()

    def testTitle(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('Busco Ayuda', self.browser.title)