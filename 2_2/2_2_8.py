import os
from selenium import webdriver
from selenium.webdriver.common.by import By


def print_answer(remote: webdriver.Remote):
    alert = remote.switch_to.alert
    print(alert.text.split()[-1])
    alert.accept()

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element(By.CSS_SELECTOR, ".form-group [name='firstname']")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.CSS_SELECTOR, ".form-group [name='lastname']")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CSS_SELECTOR, ".form-group [name='email']")
    input3.send_keys("i-petrov@mail.ru")

    element = browser.find_element(By.ID, "file")
    current_dir = os.path.abspath(os.path.dirname(__file__)) # получаем путь к директории текущего исполняемого файла
    print('current_dir - ', current_dir)
    file_path = os.path.join(current_dir, 'abc.txt') # добавляем к этому пути имя файла
    print('file_path - ', file_path)
    element.send_keys(file_path)
    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    print_answer(browser)
finally:
    browser.quit()