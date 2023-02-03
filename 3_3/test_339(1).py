import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

link = "http://selenium1py.pythonanywhere.com/"

def test_exception1():
    with webdriver.Chrome() as browser:
        browser.get(link)
        with pytest.raises(NoSuchElementException):
            browser.find_element(By.CSS_SELECTOR, "button.btn")
            pytest.fail("Не должно быть кнопки Отправить")
        
def test_exception2():
    with webdriver.Chrome() as browser:
        browser.get(link)
        with pytest.raises(NoSuchElementException):
            browser.find_element(By.CSS_SELECTOR, "no_such_button.btn")
            pytest.fail("Не должно быть кнопки Отправить")