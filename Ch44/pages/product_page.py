from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_product_to_basket(self):
        self.should_be_name_of_product()
        self.should_be_price_of_product()
        self.should_be_add_to_basket_button()

        add_to_busket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_busket_button.click()

        self.solve_quiz_and_get_code()
        self.compare_basket_and_product_name()
        self.compare_basket_and_product_price()
        print(f'Product "{self.message}" add to basket, price - {self.basket_price}')


    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), "Add to basket button not presented"


    def should_be_name_of_product(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), "Name of product don't found"


    def should_be_price_of_product(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), "Product Price not found"


    def compare_basket_and_product_name(self):
        # Проверка на сравнение названия товара и товара в корзине
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        self.message = self.browser.find_element(*ProductPageLocators.BASKET_MESSAGE).text
        assert product_name == self.message, "Product name not found on message"


    def compare_basket_and_product_price(self):
        # Сравнение цен товара и корзины
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        self.basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text
        assert product_price == self.basket_price, "Product price and basket price is not equal"

