from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/find_xpath_form"
list1 = ["Ivan", "Petrov", "Smolensk", "Russia"]

try:
    browser = webdriver.Chrome()
    browser.get(link)
    elements = browser.find_elements(By.CLASS_NAME, 'form-control')
    for num, elem in enumerate(elements):
        elem.send_keys(list1[num])

    button = browser.find_element(By.XPATH, '//button[text()="Submit"]').click()
    print(browser._switch_to.alert.text)

finally:
    browser.quit()