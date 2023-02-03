from selenium import webdriver
from time import sleep
try:
    browser = webdriver.Chrome()
    browser.execute_script("document.title='Script executing';alert('Robots at work');")
finally:
    sleep(15)
    browser.quit()