from POM.Locators.locators import Locators


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.menu_class_name = "login-button__control"
        self.logout_link_id = "login__logout"

    def click_menu(self):
        self.driver.find_element_by_class_name(self.menu_class_name).click()

    def click_logout(self):
        self.driver.find_element_by_id(Locators.logout_link_id).click()