import os
import sys
import time
import unittest
import HtmlTestRunner

# sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
# from selenium.webdriver.support.ui import Select
from dotenv.main import load_dotenv
from POM.Pages.homePage import HomePage
from POM.Pages.loginPage import LoginPage
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Vars with .env implementations
load_dotenv()
name = os.getenv("NAME")
surname = os.getenv("SURNAME")
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")
phone = os.getenv("PHONE_NUM")
test_link = os.getenv("URL")


class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):  # Choose browser driver
        # cls.driver = webdriver.Chrome(r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
        # cls.driver = webdriver.Chrome()
        cls.driver = webdriver.Firefox()
        # cls.driver = webdriver.Ie(r"C:\web_drivers\IEDriverServer.exe")
        # cls.driver = webdriver.Ie()
        driver = cls.driver
        driver.implicitly_wait(10)
        driver.maximize_window()

    # Choose browser
    # def setUp(self):
    #     # self.driver = webdriver.Chrome(r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
    #     self.driver = webdriver.Chrome()
    #     # self.driver = webdriver.Firefox()
    #     # self.driver = webdriver.Ie(r"C:\web_drivers\IEDriverServer.exe")
    #     # self.driver = webdriver.Ie()

    # Navigate to SignUp page and fill the Form
    def test_login_valid(self):
        driver = self.driver

        # * Actions on login web-page
        driver.get(test_link)
        login_page = LoginPage(driver)
        login_page.enter_login(username)
        login_page.enter_password(password)
        login_page.click_submit()

        # self.assertIn("ukr.net", driver.title)
        # # driver.maximize_window()
        # # driver.implicitly_wait(10)
        # login_field = WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.ID, "id-l"))
        # )
        # # login_field.screenshot("./login_field_image.png")
        # login_field.send_keys(login)
        # driver.find_element_by_id("id-p").send_keys(password)
        # driver.find_element_by_xpath("//button[@type='submit']").click()

        # # * Actions on home web-page
        home_page = HomePage(driver)
        home_page.click_menu()
        home_page.click_logout()

        # driver.find_element_by_class_name("login-button__control").click()
        # driver.find_element_by_id("login__logout").click()
        # # driver.save_screenshot("./mailbox_image.png")
        time.sleep(3)

    def test_login_invalid(self):
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
        testRunner=HtmlTestRunner.HTMLTestRunner(
            output="G:\\Python_autotests\\POM\\TestReports"
        )
    )
