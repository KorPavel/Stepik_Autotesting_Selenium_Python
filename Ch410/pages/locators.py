from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group > a.btn")

class BasketPageLocators:
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner > p")
    PRODUCTS_LIST_IN_BASKET = (By.CSS_SELECTOR, "#content_inner > h2")

'''
Данный класс не обязательный (локаторы в BasePageLocators)
class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
'''

class LoginPageLocators:   
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, '#add_to_basket_form > button')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main > h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main > .price_color')
    BASKET_MESSAGE = (By.CSS_SELECTOR, '#messages > :first-child > div > strong')
    BASKET_PRICE = (By.CSS_SELECTOR, '#messages > :last-child > div > p > strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > :first-child")

