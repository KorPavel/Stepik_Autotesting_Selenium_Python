from selenium import webdriver
from selenium.webdriver.common.by import By

def print_answer(remote: webdriver.Remote):
    alert = remote.switch_to.alert
    print(alert.text.split()[-1])
    alert.accept()

link_url = "http://suninjuly.github.io/wait2.html"

with webdriver.Chrome() as browser:
    browser.get(link_url)
    # говорим WebDriver искать каждый элемент в течение 5 секунд
    browser.implicitly_wait(5)

    browser.find_element(By.ID, 'verify').click()
    message = browser.find_element(By.ID, 'verify_message').text
    assert "successful" in message

