from time import sleep
import log_pass
from selenium import webdriver
from selenium.webdriver.common.by import By

LOGIN = log_pass.login
PASSWORD = log_pass.password
step_link = "https://stepik.org/lesson/567022/step/5?unit=561296"
main_page_link = "https://stepik.org/"

with webdriver.Chrome() as browser:
    browser.implicitly_wait(15)
    browser.get(main_page_link)
    browser.find_element(By.ID, 'ember234').click()
    browser.find_element(By.ID, 'id_login_email').send_keys(LOGIN)
    browser.find_element(By.ID, 'id_login_password').send_keys(PASSWORD)
    browser.find_element(By.CSS_SELECTOR, '#login_form > button').click()
    sleep(3)
    browser.get(step_link)

    browser.find_element(By.XPATH, '//span[text()="import math"]').click()
    sleep(4)
    browser.find_element(By.CSS_SELECTOR, '.submit-submission').click()
    sleep(5)
    browser.find_element(By.CSS_SELECTOR, '.lesson__next-btn').click()
    sleep(5)
