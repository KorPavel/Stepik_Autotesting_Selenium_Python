import pytest
from selenium.webdriver.common.by import By

link_lang = "http://selenium1py.pythonanywhere.com/{language}/"
link = "http://selenium1py.pythonanywhere.com/"

class TestMainPage1():
    @pytest.mark.parametrize('language', ["ru", "en-gb"])
    def test_guest_should_see_login_link(self, browser, language):
        print('\n\t\tTEST#1 - "гость должен увидеть ссылку для входа"')
        browser.get(link_lang)
        browser.find_element(By.CSS_SELECTOR, "#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        print('\n\t\tTEST#2 - "гость должен увидеть ссылку на корзину на главной странице"')
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")

    def test_guest_should_see_search_button_on_the_main_page(self, browser):
        print('\n\t\tTEST#3 - "гость должен увидеть кнопку поиска на главной странице"')
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "input.btn.btn-default")