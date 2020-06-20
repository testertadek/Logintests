import unittest
from selenium import webdriver
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))

class BaseTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('../chromedriver.exe')
        driver = self.driver
        driver.get('http://demowebshop.tricentis.com/')
        driver.maximize_window()
        driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()

if  __name__ == '__main__' :
    unittest.main()
