import os
import sys
import time
import unittest

import HtmlTestRunner.HTMLTestRunner

# import HTMLTestRunner

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from dotenv.main import load_dotenv
from POM.Pages.homePage import HomePage
from POM.Pages.loginPage import LoginPage
from selenium import webdriver

# Vars with .env implementations
load_dotenv()
name = os.getenv("NAME")
surname = os.getenv("SURNAME")
username = os.getenv("USER_NAME")
password = os.getenv("PASSWORD")
phone = os.getenv("PHONE_NUM")
test_link = os.getenv("URL")


class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):  # Choose browser driver
        # cls.driver = webdriver.Chrome()
        # cls.driver = webdriver.Firefox()
        # cls.driver = webdriver.Edge("C:/web_drivers/msedgedriver.exe")
        cls.driver = webdriver.Edge()
        driver = cls.driver
        driver.implicitly_wait(10)
        driver.maximize_window()

    # Navigate to SignUp page and fill the Form
    def test_001_login_valid(self):
        driver = self.driver

        # * Actions on login web-page
        driver.get(test_link)
        login_page = LoginPage(driver)
        login_page.enter_login(username)
        login_page.enter_password(password)
        login_page.click_submit()

        # # * Actions on home web-page
        home_page = HomePage(driver)
        home_page.click_menu()
        home_page.click_logout()
        time.sleep(3)

    def test_002_login_invalid(self):
        driver = self.driver

        # * Actions on login web-page
        driver.get(test_link)
        login_page = LoginPage(driver)
        login_page.enter_login("test123")
        login_page.enter_password(password)
        login_page.click_submit()
        message = driver.find_element_by_xpath("").text()
        self.assertEqual(message, "Неправильні дані")

    @classmethod
    def tearDown(cls):
        # self.driver.close()
        cls.driver.quit()
        print("TEST Completed")


if __name__ == "__main__":
    unittest.main(
        testRunner=HTMLTestRunner.HTMLTestRunner(
            output="G:\\Python_autotests\\POM\\TestReports"
        )
    )
