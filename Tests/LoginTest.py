from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from Logintests.Tests.BaseTest import BaseTest
from Logintests.Pages.header import Header
from Logintests.Pages.loginPage import LoginPage

valid_email = "tadeusz.kaminski21cn@gmail.com"
invalid_email = "abcd"
valid_password = "tester1"


class LoginTest(BaseTest):
    def test_valid_login(self):
        header = Header(self.driver)
        header.click_login_link()
        login = LoginPage(self.driver)
        login.enter_email(valid_email)
        login.enter_password(valid_password)
        login.click_login_button()
        self.assertEqual(header.get_user_account_name(), valid_email)


    def test_login_with_invalid_email(self):
        header = Header(self.driver)
        header.click_login_link()
        login = LoginPage(self.driver)
        login.enter_email(invalid_email)
        login.enter_password(valid_password)
        login.click_login_button()
        message = "Please enter a valid email address."
        self.assertEqual(login.get_email_error_message(), message)


if  __name__ == '__main__' :
    unittest.main()
