from .pages.basket_page import BasketPage
from .pages.product_page import ProductPage
import pytest


link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'

params = [x if x != 7 else pytest.param(x, marks=pytest.mark.xfail) for x in range(10)]

@pytest.mark.parametrize('param', params)
def test_guest_can_add_product_to_basket(browser, param):
    '''Тест-кейс проверяет ряд промо-кодов, среди которых есть баг, который нужно отметить xfail '''
    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{param}'

    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_product_to_basket()
    product_page.compare_basket_and_product_name()
    product_page.compare_basket_and_product_price()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    '''Тест-кейс проверяет, что после добавления товара в корзину не должно быть сообщения об этом '''
    print('\n\t\tTEST#1 "Guest cant see success message after adding product to basket"')
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_product_to_basket()
    product_page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    '''Тест-кейс проверяет, что перед добавлением товара в корзину нет никакого сообщения '''
    print('\n\t\tTEST#2 "Guest cant see success message"')
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_not_be_success_message()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    '''Тест-кейс проверяет, что после добавления товара в корзину сообщение об этом исчезает '''
    print('\n\t\tTEST#3 "Message disappeared after adding product to basket"')
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_product_to_basket()
    product_page.should_be_success_message_disappeared()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    '''Тест-кейс открывает страницу корзины, проверяет отсутствие товаров в ней 
       и сообщение о пустой корзине '''
    print('\n\t\tTEST#4 "Guest cant see product in basket opened from product page"')
    product_page = ProductPage(browser, link) 
    product_page.open()
    product_page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_products_in_basket()
    basket_page.message_about_empty_basket_is_presented()






