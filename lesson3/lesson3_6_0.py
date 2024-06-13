import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize("lesson", [236895, 236896, 236897, 236898, 236899, 236903, 236904, 236905])
def test_time(browser, lesson):
    browser.get(f"https://stepik.org/lesson/{lesson}/step/1")
    time.sleep(3)
    browser.find_element(By.ID, "ember459").click()
    browser.find_element(By.ID, "id_login_email").send_keys("**************@gmail.com")
    browser.find_element(By.ID, "id_login_password").send_keys("*************")
    browser.find_element(By.CSS_SELECTOR, ".sign-form__btn").click()
    time.sleep(30)
    browser.find_element(By.TAG_NAME, "textarea").send_keys(math.log(int(time.time())))
    browser.find_element(By.CSS_SELECTOR, ".submit-submission").click()
    assert browser.find_element(By.CSS_SELECTOR, ".smart-hints__hint").text == "Correct!"