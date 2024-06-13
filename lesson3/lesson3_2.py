from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

class TestReg(unittest.TestCase):
    def test_reg1(self):
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/registration1.html")

        browser.find_element(By.CSS_SELECTOR, ".first_block .first").send_keys("Clarence")
        browser.find_element(By.CSS_SELECTOR, ".first_block .second").send_keys("Fishman")
        browser.find_element(By.CSS_SELECTOR, ".first_block .third").send_keys("determinant666@gmail.com")
        browser.find_element(By.CSS_SELECTOR, ".second_block .first").send_keys("18005552633")
        browser.find_element(By.CSS_SELECTOR, ".second_block .second").send_keys("Moscow, General White St., 6")

        browser.find_element(By.CSS_SELECTOR, "button.btn").click()

        self.assertEqual(browser.find_element(By.TAG_NAME, "h1").text, "Congratulations! You have successfully registered!", "One of elements not found")

    def test_reg2(self):
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/registration2.html")

        browser.find_element(By.CSS_SELECTOR, ".first_block .first").send_keys("Clarence")
        browser.find_element(By.CSS_SELECTOR, ".first_block .second").send_keys("Fishman")
        browser.find_element(By.CSS_SELECTOR, ".first_block .third").send_keys("determinant666@gmail.com")
        browser.find_element(By.CSS_SELECTOR, ".second_block .first").send_keys("18005552633")
        browser.find_element(By.CSS_SELECTOR, ".second_block .second").send_keys("Moscow, General White St., 6")

        browser.find_element(By.CSS_SELECTOR, "button.btn").click()

        self.assertEqual(browser.find_element(By.TAG_NAME, "h1").text, "Congratulations! You have successfully registered!", "One of elements not found")

if __name__ == "__main__":
    unittest.main()