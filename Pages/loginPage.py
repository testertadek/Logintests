class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.email_textbox_id = "Email"
        self.password_textbox_id = "Password"
        self.login_button_class = "login-button"
        self.email_validation_messagge_xpath = "//span[@for ='Email']"


    def enter_email(self, email):
        self.driver.find_element_by_id(self.email_textbox_id).clear()
        self.driver.find_element_by_id(self.email_textbox_id).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element_by_id(self.password_textbox_id).clear()
        self.driver.find_element_by_id(self.password_textbox_id).send_keys(password)

    def click_login_button(self):
        self.driver.find_element_by_class_name(self.login_button_class).click()

    def get_email_error_message(self):
        message = self.driver.find_element_by_xpath(self.email_validation_messagge_xpath).text
        return message
