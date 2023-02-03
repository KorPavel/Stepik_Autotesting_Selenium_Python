import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestMainPage1():

    def test_guest_should_see_login_link(self, browser):
        print('\n\t\tTEST#1 - "гость должен увидеть ссылку для входа"')
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        print('\n\t\tTEST#2 - "гость должен увидеть ссылку на корзину на главной странице"')
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")

    @pytest.mark.xfail(reason="Данный баг исправлен!")
    def test_guest_should_see_search_button_on_the_main_page(self, browser):
        print('\n\t\tTEST#3 - "гость должен увидеть кнопку поиска на главной странице"')
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "input.btn.btn-default")