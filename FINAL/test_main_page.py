from .pages.basket_page import BasketPage
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
import pytest


link = "http://selenium1py.pythonanywhere.com/"

class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser):
        """Тест-кейс открывает страницу Входа/Регистрации, проверяет наличие элементов
           (форма входа, форма регистрации, корректность URL-адреса) """
        print('\n\t\tTEST#1 "Guest can go to login page"')
        page = MainPage(browser, link) 
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()
    
    
    def test_guest_should_see_login_link(self, browser):
        """Тест-кейс проверяет наличие ссылки на страницу Входа/Регистрации """
        print('\n\t\tTEST#2 "Guest should see login link"')
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    '''Тест-кейс открывает страницу корзины, проверяет отсутствие товаров в ней 
       и сообщение о пустой корзине '''
    print('\n\t\tTEST#3 "Guest cant see product in basket opened from main page"')
    page = MainPage(browser, link) 
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_products_in_basket()
    basket_page.message_about_empty_basket_is_presented()

