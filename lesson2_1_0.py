from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/math.html")

    x = browser.find_element(By.ID, "input_value").text
    browser.find_element(By.CSS_SELECTOR, ".form-control").send_keys(calc(x))

    browser.find_element(By.CSS_SELECTOR, "[type='checkbox']").click()
    browser.find_element(By.CSS_SELECTOR, "[value='robots']").click()
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    time.sleep(1)

finally:
    time.sleep(10)
    browser.quit()
