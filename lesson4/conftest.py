import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None, help="Choose language")

@pytest.fixture(scope="function")
def browser(request):
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.implicitly_wait(5)
    lang = request.config.getoption("language")
    browser.get(f"http://selenium1py.pythonanywhere.com/{lang}")
    yield browser
    print("\nquit browser..")
    browser.quit()
