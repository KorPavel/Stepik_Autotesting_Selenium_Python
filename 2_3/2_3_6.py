import math
from selenium import webdriver
from selenium.webdriver.common.by import By

def print_answer(remote: webdriver.Remote):
    alert = remote.switch_to.alert
    print(alert.text.split()[-1])
    alert.accept()

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link_url = 'http://suninjuly.github.io/redirect_accept.html'

with webdriver.Chrome() as browser:
    browser.get(link_url)
    browser.find_element(By.CLASS_NAME, 'trollface').click()
    new_window = browser.window_handles[1]
    # print(new_window)
    browser.switch_to.window(new_window)
    num = int(browser.find_element(By.ID, 'input_value').text)
    browser.find_element(By.ID, 'answer').send_keys(calc(num))
    browser.find_element(By.CSS_SELECTOR, 'button.btn').click()
    print_answer(browser)
