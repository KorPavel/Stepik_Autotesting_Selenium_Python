import math
from selenium import webdriver
from selenium.webdriver.common.by import By

link_text = str(math.ceil(math.pow(math.pi, math.e)*10000))
url = 'http://suninjuly.github.io/find_link_text'
inputs = ['Name', 'Surname', 'City', 'Country']

with webdriver.Chrome() as browser:
    browser.get(url)
    browser.find_element(By.LINK_TEXT, link_text).click()
    elements = browser.find_elements(By.CLASS_NAME, 'form-control')
    [el.send_keys(text) for el, text in zip(elements, inputs)]
    browser.find_element(By.CLASS_NAME, 'btn').click()
    print(browser._switch_to.alert.text)