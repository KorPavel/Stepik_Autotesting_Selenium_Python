from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep

url = 'http://suninjuly.github.io/selects1.html'
# url = 'http://suninjuly.github.io/selects2.html'

with webdriver.Chrome() as browser:
    browser.get(url)
    num = sum(map(int, (browser.find_element(By.ID, f'num{i}').text for i in '12')))
    Select(browser.find_element(By.TAG_NAME, 'select')).select_by_value(str(num))
    browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()
    print(browser.switch_to.alert.text)
    sleep(5)
