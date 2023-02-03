from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

selectors = ['first', 'third', 'second']
texts = ['Ivan', 'Petrov', 'i-petrov@mail.ru']
text_reg = "Congratulations! You have successfully registered!"
text_err = "something went wrong"

def linked(link):
    browser.get(link)
    for sel, txt in zip(selectors, texts):
        browser.find_element(By.CSS_SELECTOR, '.first_block .' + sel).send_keys(txt)
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    registred = browser.find_element(By.TAG_NAME, "h1")
    return registred.text

class RegTest(unittest.TestCase):

    def test_link1(self):
        link = "http://suninjuly.github.io/registration1.html"
        welcome_text = linked(link)
        self.assertEqual(text_reg, welcome_text, text_err)

    def test_link2(self):
        link = "http://suninjuly.github.io/registration2.html"
        welcome_text = linked(link)
        self.assertEqual(text_reg, welcome_text, text_err)


if __name__ == '__main__':
    try:
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        unittest.main()
    finally:
        browser.quit()