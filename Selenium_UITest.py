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

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("https://pypi.org/")

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.NAME, "q")))

        search_element_by_name = driver.find_element(By.NAME, "q")
        search_element_by_name.send_keys("Can Birlik")
        search_element_by_name.send_keys(Keys.ENTER)

        assert "There were no results for" not in driver.page_source

    def tearDown(self) -> None:
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
