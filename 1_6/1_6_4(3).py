from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/simple_form_find_task.html"

with webdriver.Chrome() as browser:
    browser.get(link)
    browser.find_element(By.NAME, 'first_name').send_keys('First Name')
    browser.find_element(By.NAME, 'last_name').send_keys('Last Name')
    browser.find_element(By.NAME, 'firstname').send_keys('City')
    browser.find_element(By.ID, 'country').send_keys('Country')
    browser.find_element(By.ID, 'submit_button').click()
    print('Answer: ', browser._switch_to.alert.text.split()[-1])