from time import sleep
import log_pass
from selenium import webdriver
from selenium.webdriver.common.by import By

LOGIN = log_pass.login
PASSWORD = log_pass.password
step_link = "https://stepik.org/lesson/567021/step/14?unit=561295"
main_page_link = "https://stepik.org/"

def arifm(x, y, op):
    res = ''
    if op in '+-*/':
        res = eval(x + op + y)
        print(f'{x} {op} {y} = {res}')
    else:
        print('Неверный оператор')
    return res


with webdriver.Chrome() as browser:
    browser.implicitly_wait(15)
    browser.get(main_page_link)
    browser.find_element(By.ID, 'ember234').click()
    browser.find_element(By.ID, 'id_login_email').send_keys(LOGIN)
    browser.find_element(By.ID, 'id_login_password').send_keys(PASSWORD)
    browser.find_element(By.CSS_SELECTOR, '#login_form > button').click()
    sleep(3)
    browser.get(step_link)
    lesson = browser.find_element(By.CSS_SELECTOR,
                                  '.top-tools__lesson-name').text
    print(lesson)
    while 'операции' in lesson:
        primer = browser.find_element(By.CSS_SELECTOR, 'code.hljs').text.split('\n')
        x = primer[0].split()[-1]
        y = primer[1].split()[-1]
        op = primer[1].split()[1][0]
        browser.find_element(By.CSS_SELECTOR,
                             '.number-quiz__input').send_keys(arifm(x, y, op))
        browser.find_element(By.CSS_SELECTOR, '.submit-submission').click()
        sleep(4)
        browser.find_element(By.CSS_SELECTOR, '.lesson__next-btn').click()
        sleep(5)
        lesson = browser.find_element(By.CSS_SELECTOR,
                                      '.top-tools__lesson-name').text