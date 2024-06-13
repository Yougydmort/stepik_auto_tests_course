from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/registration1.html")

    browser.find_element(By.CSS_SELECTOR, ".first_block .first").send_keys("Clarence")
    browser.find_element(By.CSS_SELECTOR, ".first_block .second").send_keys("Fishman")
    browser.find_element(By.CSS_SELECTOR, ".first_block .third").send_keys("determinant666@gmail.com")
    browser.find_element(By.CSS_SELECTOR, ".second_block .first").send_keys("18005552633")
    browser.find_element(By.CSS_SELECTOR, ".second_block .second").send_keys("Moscow, General White St., 6")
    time.sleep(5)

    browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    time.sleep(1)

    assert browser.find_element(By.TAG_NAME, "h1").text == "Congratulations! You have successfully registered!"

finally:
    time.sleep(10)
    browser.quit()
