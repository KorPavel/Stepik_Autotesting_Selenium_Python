import math
from selenium import webdriver
from selenium.webdriver.common.by import By

def print_answer(remote: webdriver.Remote):
    alert = remote.switch_to.alert
    print(alert.text.split()[-1])
    alert.accept()

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link_url = 'http://suninjuly.github.io/alert_accept.html'

with webdriver.Chrome() as browser:
    browser.get(link_url)
    browser.find_element(By.CLASS_NAME, 'btn').click()
    browser.switch_to.alert.accept()
    num = int(browser.find_element(By.ID, 'input_value').text)
    browser.find_element(By.ID, 'answer').send_keys(calc(num))
    browser.find_element(By.CSS_SELECTOR, 'button.btn').click()
    print_answer(browser)
