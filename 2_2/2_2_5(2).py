from selenium import webdriver
from selenium.webdriver.common.by import By
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

def print_answer(remote: webdriver.Remote):
    alert = remote.switch_to.alert
    print(alert.text.split()[-1])
    alert.accept()

try: 
    link = "https://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element(By.ID, 'input_value').text

    input1 = browser.find_element(By.ID, 'answer').send_keys(calc(x))

    button1 = browser.find_element(By.ID, 'robotCheckbox')
    button1.location_once_scrolled_into_view
    button1.click()
    
    button2 = browser.find_element(By.ID, 'robotsRule')
    button2.location_once_scrolled_into_view
    button2.click()
    
    button3 = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button3.location_once_scrolled_into_view
    button3.click()

    print_answer(browser)
finally:
    browser.quit()