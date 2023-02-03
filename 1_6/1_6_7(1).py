from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'http://suninjuly.github.io/huge_form.html'
with webdriver.Chrome() as browser:
    browser.get(url)
    fields = browser.find_elements(By.TAG_NAME, 'input')
    [el.send_keys(f'my text {i}') for i, el in enumerate(fields, 1)]
    browser.find_element(By.CLASS_NAME, 'btn').click()
    print(browser._switch_to.alert.text)