from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/execute_script.html")

    x = browser.find_element(By.ID, "input_value").text
    browser.find_element(By.ID, "answer").send_keys(calc(x))

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    browser.find_element(By.CSS_SELECTOR, "[type='checkbox']").click()
    browser.find_element(By.CSS_SELECTOR, "[value='robots']").click()
    button.click()
    time.sleep(1)

finally:
    time.sleep(10)
    browser.quit()
