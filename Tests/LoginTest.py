


from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from Logintests.Pages.header import Header
from Logintests.Pages.loginPage import LoginPage


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome('./chromedriver.exe')
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_valid_login(self):
        driver = self.driver
        driver.get("http://demowebshop.tricentis.com/")
        header = Header(driver)
        header.click_login_link()

        login = LoginPage(driver)
        email = "tadeusz.kaminski21cn@gmail.com"
        login.enter_email(email)
        login.enter_password("tester1")
        login.click_login_button()

        self.assertEqual(header.get_user_account_name(), email)
        header.logout()

    def test_zlogin_with_invalid_email(self):
        driver = self.driver
        driver.get("http://demowebshop.tricentis.com/")
        header = Header(driver)
        header.click_login_link()

        login = LoginPage(driver)
        login.enter_email("abcd")
        login.enter_password("tester1")
        login.click_login_button()
        message = "Please enter a valid email address."
        self.assertEqual(login.get_email_error_message(), message)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test completed")

if  __name__ == '__main__' :
    unittest.main()
