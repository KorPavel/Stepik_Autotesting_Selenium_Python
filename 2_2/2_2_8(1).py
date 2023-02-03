import os
from selenium import webdriver
from selenium.webdriver.common.by import By

def print_answer(remote: webdriver.Remote):
    alert = remote.switch_to.alert
    print(alert.text.split()[-1])
    alert.accept()

file_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'data.txt')

if not os.path.exists(file_path):
    with open(file_path, 'w') as f:
        print('Selenium - rulezz =)', file=f)

inputs = ['Ivan', 'Petrov', 'i-petrov@mail.ru', file_path]

with webdriver.Chrome() as browser:
    browser.get('http://suninjuly.github.io/file_input.html')
    for element, value in zip(browser.find_elements(By.TAG_NAME, 'input'), inputs):
        element.send_keys(value)

    browser.find_element(By.CSS_SELECTOR, 'button.btn').click()
    print_answer(browser)
