from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
import pytest



link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-cathedral-the-bazaar_190/"

class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/accounts/login/"
        page = LoginPage(browser, link)
        page.open()
        page.register_new_user()
        page.should_be_authorized_user()
    
    
    def test_user_cant_see_success_message(self, browser):
        '''Тест-кейс проверяет, что перед добавлением товара в корзину нет никакого сообщения '''
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
        print('\n\t\tTEST# "User cant see success message"')
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.should_not_be_success_message()
    
    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        '''Тест-кейс проверяет соответствие названия товара и его цены, добавленного в корзину'''
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        print('\n\t\tTEST# "User can add product to basket"')
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.add_product_to_basket()
        product_page.compare_basket_and_product_name()
        product_page.compare_basket_and_product_price()


@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    '''Тест-кейс проверяет соответствие названия товара и его цены, добавленного в корзину'''
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    print('\n\t\tTEST# "Guest can add product to basket"')
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_product_to_basket()
    product_page.compare_basket_and_product_name()
    product_page.compare_basket_and_product_price()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    '''Тест-кейс проверяет, что после добавления товара в корзину сообщение об этом исчезает '''
    print('\n\t\tTEST# "Message disappeared after adding product to basket"')
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_product_to_basket()
    product_page.should_be_success_message_disappeared()

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    '''Тест-кейс проверяет, что после добавления товара в корзину не должно быть сообщения об этом '''
    print('\n\t\tTEST# "Guest cant see success message after adding product to basket"')
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_product_to_basket()
    product_page.should_not_be_success_message()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    '''Тест-кейс открывает страницу корзины, проверяет отсутствие товаров в ней 
       и сообщение о пустой корзине '''
    print('\n\t\tTEST# "Guest cant see product in basket opened from product page"')
    product_page = ProductPage(browser, link) 
    product_page.open()
    product_page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_products_in_basket()
    basket_page.message_about_empty_basket_is_presented()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    """Тест-кейс открывает страницу Входа/Регистрации, проверяет наличие элементов
       (форма входа, форма регистрации, корректность URL-адреса) """
    print('\n\t\tTEST# "Guest can go to login page from product page"')
    page = ProductPage(browser, link) 
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()




