from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://canbirlik.com")

WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, "/html/body/div/div/section/article[2]/a")))

certifications = driver.find_element(By.XPATH, "/html/body/div/div/section/article[2]/a")
certifications.click()

WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, "/html/body/div/div/section[2]/div/div/table/tbody")))

certification_list = driver.find_element(By.XPATH, "/html/body/div/div/section[2]/div/div/table/tbody")
print(f"Can Birlik has {len(certification_list.text.splitlines())} certifications.")

time.sleep(10)