import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption("--language", action="store")

@pytest.fixture(scope="function")
def browser(request):
    print("\nstart browser for test..")
    experimental_options = Options()
    experimental_options.add_experimental_option("prefs", {"intl.accept_languages": request.config.getoption("language")})
    browser = webdriver.Chrome(options = experimental_options)
    yield browser
    print("\nquit browser..")
    browser.quit()