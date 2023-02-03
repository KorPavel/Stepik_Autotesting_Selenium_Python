import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

reg_text = 'Congratulations! You have successfully registered!'

def linked(link):
    with webdriver.Chrome() as browser:
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".first_block .first").send_keys('Ivan')
        browser.find_element(By.CSS_SELECTOR, ".first_block .third").send_keys('i-petrov@mail.ru')
        browser.find_element(By.CSS_SELECTOR, ".first_block .second").send_keys('Petrov')
        browser.find_element(By.CSS_SELECTOR, "button.btn").click()
        result = WebDriverWait(browser, 5).until(
            expected_conditions.presence_of_element_located((By.TAG_NAME, "h1"))).text
    return result

class TestRegistered(unittest.TestCase):
    def test_reg1(self):
        link1 = 'http://suninjuly.github.io/registration1.html'
        self.assertEqual(linked(link1), reg_text, 'No registred!')

    def test_reg2(self):
        link2 = 'http://suninjuly.github.io/registration2.html'
        self.assertEqual(linked(link2), reg_text, 'No registred!')

if __name__ == "__main__":
    unittest.main()