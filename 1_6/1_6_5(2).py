import time
import math
import log_pass
from selenium import webdriver
from selenium.webdriver.common.by import By

LOGIN = log_pass.login
PASSWORD = log_pass.password
link = "http://suninjuly.github.io/find_link_text"
step_link = "https://stepik.org/lesson/138920/step/5"
main_page_link = "https://stepik.org/"
value = str(math.ceil(math.pow(math.pi, math.e)*10000))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element(By.LINK_TEXT, value)
    button.click()

    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CLASS_NAME, "city")
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    alert = browser.switch_to.alert
    answer = alert.text.split()[-1]
    time.sleep(3)
    alert.accept()
    browser.get(main_page_link)
    time.sleep(3)
    sign_in_button = browser.find_element(By.LINK_TEXT, "Войти")
    sign_in_button.click()
    time.sleep(3)
    login = browser.find_element(By.NAME, "login")
    password = browser.find_element(By.NAME, "password")
    pop_up_sign_in_button = browser.find_element(By.CSS_SELECTOR, "button.sign-form__btn.button_with-loader ")
    login.send_keys(LOGIN)
    password.send_keys(PASSWORD)
    time.sleep(3)
    pop_up_sign_in_button.click()
    time.sleep(4)
    browser.get(step_link)
    time.sleep(10)
    textarea = browser.find_element(By.TAG_NAME, "textarea")
    textarea.send_keys(answer)
    time.sleep(2)
    send_button = browser.find_element(By.CLASS_NAME, "submit-submission")
    send_button.click()
    time.sleep(15)

finally:
    browser.quit()