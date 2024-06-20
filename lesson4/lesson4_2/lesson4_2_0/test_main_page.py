from .pages.main_page import MainPage

def test_guest_should_see_login_link(browser):
    MainPage(browser, "http://selenium1py.pythonanywhere.com/").open()
    MainPage(browser, "http://selenium1py.pythonanywhere.com/").should_be_login_link()

def test_guest_can_go_to_login_page(browser):
    MainPage(browser, "http://selenium1py.pythonanywhere.com/").open()
    MainPage(browser, "http://selenium1py.pythonanywhere.com/").go_to_login_page()
