from selenium.webdriver.common.by import By
from time import sleep

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_should_see_add_to_basket_button(browser):
    print('\n\t\tTEST#1 "Add to basket button"')
    browser.get(link)
    try:
        basket_button = browser.find_element(By.CSS_SELECTOR, "#add_to_basket_form button")
    finally:
        assert basket_button, "неверный селектор кнопки"
    

def test_guest_should_see_text_on_add_to_basket_button(browser):
    print('\n\t\tTEST#2 "The guest should see the text on the add to cart button in French"')
    browser.get(link)
    sleep(4)
    text_btn = browser.find_element(By.CSS_SELECTOR, "#add_to_basket_form button").text
    assert text_btn == 'Ajouter au panier'