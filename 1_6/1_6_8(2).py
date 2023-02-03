from selenium import webdriver
from selenium.webdriver.common.by import By

link = 'http://suninjuly.github.io/find_xpath_form'
with webdriver.Chrome() as browser:
    browser.get(link)
    inputs = ['Name', 'Surname', 'City', 'Country']
    elements = browser.find_elements(By.CLASS_NAME, 'form-control')
    [el.send_keys(text) for el, text in zip(elements, inputs)]
    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    print(browser._switch_to.alert.text)