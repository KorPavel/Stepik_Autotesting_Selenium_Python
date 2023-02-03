from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

def print_answer(remote: webdriver.Remote):
    alert = remote.switch_to.alert
    print(alert.text.split()[-1])
    alert.accept()

link_url = "http://suninjuly.github.io/wait1.html"

with webdriver.Chrome() as browser:
    browser.get(link_url)
    sleep(3)
    browser.find_element(By.ID, 'verify').click()
    
    msg = browser.find_element(By.ID, 'verify_message').text
    assert "successful" in msg

