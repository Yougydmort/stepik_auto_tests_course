from .pages.main_page import MainPage

def test_guest_should_see_login_link(browser):
    MainPage(browser, "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer").open()
    MainPage(browser, "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer").should_be_login_link()

def test_guest_can_go_to_login_page(browser):
    MainPage(browser, "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer").open()
    MainPage(browser, "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer").go_to_login_page()
