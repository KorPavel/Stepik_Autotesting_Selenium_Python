import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


# ссылки заданий
link1 = "http://suninjuly.github.io/registration1.html"
link2 = "http://suninjuly.github.io/registration2.html"

# значения для заполнения полей формы регистрации
first_name = "Ivan"
last_name = "Petrov"
email = "i-petrov@mail.ru"

# Ожидаемое значение в заголовке страницы после регистрации
EXPECTED_ANS = "Congratulations! You have successfully registered!"

def send_form(link) -> str:
    """
    функция заполнения формы регистрации
    возвращает строку заголовка страницы после регистрации
    """
    # browser закроется после выполнения скрипта сам
    with webdriver.Chrome() as browser:
        browser.get(link)

        # код, который заполняет обязательные поля
        browser.find_element(By.CSS_SELECTOR, ".first_block .first").send_keys(first_name)
        browser.find_element(By.CSS_SELECTOR, ".first_block .second").send_keys(last_name)
        browser.find_element(By.CSS_SELECTOR, ".first_block .third").send_keys(email)

        # Отправляем заполненную форму
        browser.find_element(By.CSS_SELECTOR, "button.btn").click()

        # Проверяем, что смогли зарегистрироваться
        # ожидаем появление элемента "заголовок страницы", содержащего текст
        welcome_text_elt = WebDriverWait(browser, 10).until(
            expected_conditions.presence_of_element_located((By.TAG_NAME, "h1")))

        # записываем полученный текст в переменную
        return welcome_text_elt.text


# класс для тестов
class TestLinksRegistration(unittest.TestCase):
    def test_link1(self):
        received_ans1 = send_form(link1)
        self.assertEqual(EXPECTED_ANS, received_ans1, "Test1: Text in H1 does not match.")

    def test_link2(self):
        received_ans2 = send_form(link2)
        self.assertEqual(EXPECTED_ANS, received_ans2, "Test2: Text in H1 does not match.")


if __name__ == "__main__":
    unittest.main()