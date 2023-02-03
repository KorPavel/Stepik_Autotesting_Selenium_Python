import math
from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'http://SunInJuly.github.io/execute_script.html'

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

with webdriver.Chrome() as browser:
    browser.get(url)
    answer = calc(browser.find_element(By.ID, 'input_value').text)
    browser.find_element(By.ID, 'answer').send_keys(answer)
    controls = [browser.find_element(By.ID, 'robotCheckbox'),
                browser.find_element(By.ID, 'robotsRule'),
                browser.find_element(By.CSS_SELECTOR, '[type="submit"]')]
    for el in controls:
        el.location_once_scrolled_into_view
        el.click()

    print(browser.switch_to.alert.text)