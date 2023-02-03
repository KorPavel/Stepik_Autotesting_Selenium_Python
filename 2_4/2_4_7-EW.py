from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

def print_answer(remote: webdriver.Remote):
    alert = remote.switch_to.alert
    print(alert.text.split()[-1])
    alert.accept()

link_url = "http://suninjuly.github.io/wait2.html"

with webdriver.Chrome() as browser:
    browser.get(link_url)
    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.ID, "verify"))).click()

    message = browser.find_element(By.ID, 'verify_message').text
    assert "successful" in message

