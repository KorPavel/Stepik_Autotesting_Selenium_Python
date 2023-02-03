from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_product_to_basket(self):
        '''Тест-кейс сначала проверяет наличие элементов (название товара, цена товара, 
           кнопка добавления в корзину). Далее кликает по кнопке, и решает математическую задачу '''
        self.should_be_name_of_product()
        self.should_be_price_of_product()
        self.should_be_add_to_basket_button()

        add_to_busket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_busket_button.click()

        self.solve_quiz_and_get_code()


    def should_be_add_to_basket_button(self):
        '''Проверка наличия элемента '''
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), \
            "Add to basket button not presented"


    def should_be_name_of_product(self):
        '''Проверка наличия элемента '''
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), \
            "Name of product don't found"


    def should_be_price_of_product(self):
        '''Проверка наличия элемента '''
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), \
            "Product Price not found"


    def compare_basket_and_product_name(self):
        # Проверка на сравнение названия товара и товара в корзине
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        message = self.browser.find_element(*ProductPageLocators.BASKET_MESSAGE).text
        print(f'Product "{message}" add to basket, ', end='')
        assert product_name == message, "Product name not found on message"


    def compare_basket_and_product_price(self):
        # Сравнение цен товара и корзины
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text
        print(f'price - {basket_price}')
        assert product_price == basket_price, "Product price and basket price is not equal"

    def should_not_be_success_message(self):
        '''Проверка отсутствия элемента '''
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_success_message_disappeared(self):
        '''Проверка исчезновения элемента '''
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not disappeared, but should disappear"







