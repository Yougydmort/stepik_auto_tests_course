import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Ma-a-an… I wish they had it in English too…
@pytest.mark.parametrize("language", ["en", "es", "fr", "it", "pl", "el"])
def test_find_add_to_cart_btn(browser, language):
    browser.get(f"http://selenium1py.pythonanywhere.com/{language}/catalogue/coders-at-work_207/")
    time.sleep(30)
    assert browser.find_element(By.CLASS_NAME, "btn-add-to-basket").is_displayed(), "Button not found"
