from POM.Locators.locators import Locators


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.login_field_id = "id-l"
        self.password_field_id = "id-p"
        self.submit_button_xpath = "//button[@type='submit']"
        self.invalid_login_message_xpath = "//p[@class='form__error form__error_fail']"

    def enter_login(self, login):
        self.driver.find_element_by_id(self.login_field_id).clear()
        self.driver.find_element_by_id(Locators.login_field_id).send_keys(
            login
        )  # see implementation of imported Locators

    def enter_password(self, password):
        self.driver.find_element_by_id(self.password_field_id).clear()
        self.driver.find_element_by_id(self.password_field_id).send_keys(password)

    def click_submit(self):
        self.driver.find_element_by_xpath(self.submit_button_xpath).click()

    def check_invalid_login(self, message):
        msg = self.driver.find_element_by_xpath(self.invalid_login_message_xpath).text()
        return msg