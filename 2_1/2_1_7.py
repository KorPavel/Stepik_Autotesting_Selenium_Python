import math
from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


def print_answer(remote: webdriver.Remote):
    alert = remote.switch_to.alert
    print(alert.text.split()[-1])
    alert.accept()


browser = webdriver.Chrome()
link = "http://suninjuly.github.io/get_attribute.html"
browser.get(link)

try:
    x = browser.find_element(By.ID, 'treasure').get_attribute("valuex")
    browser.find_element(By.ID, "answer").send_keys(calc(x))
    elements_to_select = ["#robotCheckbox", "#robotsRule", "button.btn.btn-default"]

    for elem in elements_to_select:
        browser.find_element(By.CSS_SELECTOR, elem).click()

    print_answer(browser)
finally:
    browser.quit()