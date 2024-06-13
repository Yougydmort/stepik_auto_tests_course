from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/find_xpath_form.html")

    browser.find_element(By.TAG_NAME, "input").send_keys("Clarence")
    browser.find_element(By.NAME, "last_name").send_keys("Fishman")
    browser.find_element(By.CLASS_NAME, "city").send_keys("Moscow")
    browser.find_element(By.ID, "country").send_keys("Russia")
    browser.find_element(By.XPATH, "//button[@type='submit']").click()

finally:
    time.sleep(30)
    browser.quit()
