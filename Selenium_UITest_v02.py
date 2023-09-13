import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class SeleniumUITestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_unicorn_items(self):
        driver = self.driver
        driver.get("http://unicornitems.com/my-account/")

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.NAME, "username")))

        search_element_by_name_1 = driver.find_element(By.NAME, "username")
        search_element_by_name_1.send_keys("q")

        search_element_by_name_2 = driver.find_element(By.NAME, "password")
        search_element_by_name_2.send_keys("q")

        button = driver.find_element(By.NAME, "login")
        button.click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "woocommerce-error")))

        alert_message = driver.find_element(By.CLASS_NAME, "woocommerce-error")
        assert "ERROR" in alert_message.text

    def tearDown(self) -> None:
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
