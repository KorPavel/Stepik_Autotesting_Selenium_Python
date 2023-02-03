from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

def print_answer(remote: webdriver.Remote):
    alert = remote.switch_to.alert
    print(alert.text.split()[-1])
    alert.accept()

try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x1 = browser.find_element(By.ID, 'num1').text
    x2 = browser.find_element(By.ID, 'num2').text
    Select(browser.find_element(By.ID, "dropdown")).select_by_visible_text(str(int(x1) + int(x2)))

    button3 = browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    print_answer(browser)
finally:
    browser.quit()