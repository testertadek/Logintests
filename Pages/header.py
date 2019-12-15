class Header:

    def __init__(self, driver):
        self.driver = driver
        self.login_link_xpath ="//div[contains(@class, 'header')]//a[contains(@class, 'ico-login')]"
        self.customer_data_link_xpath = "//div[contains(@class, 'header')]//a[contains(@class, 'account')]"
        self.log_out_link_xpath = "//div[contains(@class, 'header')]//a[contains(@class, 'ico-logout')]"

    def click_login_link(self):
        self.driver.find_element_by_xpath(self.login_link_xpath).click()

    def get_user_account_name(self):
        user_data_link = self.driver.find_element_by_xpath(self.customer_data_link_xpath)
        user_data = user_data_link.text
        return user_data

    def logout(self):
        self.driver.find_element_by_xpath(self.log_out_link_xpath).click()
