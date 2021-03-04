import time
import unittest

from selenium import webdriver
from selenium.common.exceptions import (
    ElementNotSelectableException,
    ElementNotVisibleException,
)
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class PythonOrgSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        # self.driver = webdriver.Chrome()
        # self.driver = webdriver.Edge(executable_path='C:\web_drivers\msedgedriver.exe')
        # self.driver = webdriver.Android()

    # def document_initialized(self, driver):
    #     return self.driver.execute_script("return initialized")
    # #touchnav-wrapper > header > div > div.options-bar-container.do-not-print > a

    def test_search_in_python_org(self):
        driver = self.driver
        actions = ActionChains(driver)
        driver.get("https://www.python.org/")
        # WebDriverWait(driver, timeout=5).until(self.document_initialized)
        self.assertIn("Python", driver.title)
        driver.maximize_window()
        elem = driver.find_element_by_name("q")
        # assert elem.text == "Donate"
        elem.screenshot("./elem_test_image.png")
        elem.send_keys(f"selenium {Keys.RETURN}")
        # print(Keys.RETURN, "Keys.RETURN")
        time.sleep(5)
        driver.save_screenshot("./test_image.png")
        # actions.pause(5)

    # def show_alert(self):
    #     driver = self.driver
    #     wait = WebDriverWait(
    #         driver,
    #         10,
    #         poll_frequency=1,
    #         ignored_exceptions=[
    #             ElementNotVisibleException,
    #             ElementNotSelectableException,
    #         ],
    #     )
    #     driver.find_element(By.LINK_TEXT, "Donate").click()
    #     alert = wait.until(EC.alert_is_present())
    #     text = alert.text
    #     if text:
    #         print(text)
    #         alert.accept()
    #     else:
    #         print("Alert is not been shown")

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
