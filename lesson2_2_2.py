from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/file_input.html")

    browser.find_element(By.NAME, "firstname").send_keys("Clarence")
    browser.find_element(By.NAME, "lastname").send_keys("Fishman")
    browser.find_element(By.NAME, "email").send_keys("determinant666@gmail.com")
    browser.find_element(By.ID, "file").send_keys(os.path.join(os.path.abspath(os.path.dirname(__file__)), "pythonrulez.txt"))

    browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    time.sleep(1)

finally:
    time.sleep(10)
    browser.quit()
