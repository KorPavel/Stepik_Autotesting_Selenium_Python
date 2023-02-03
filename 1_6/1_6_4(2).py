import time
from selenium import webdriver

link = "http://suninjuly.github.io/simple_form_find_task.html"

browser = webdriver.Chrome()
browser.get(link)

try:
    dict = (
        {"css":"input[name='first_name']", "text":"Ivan"},
        {"css":"input[name='last_name']", "text": "Petrov"},
        {"css":".city", "text":"Smolensk"},
        {"css":"#country", "text":"Russia"}
    )

    for element in dict:
        textarea = browser.find_element_by_css_selector(element["css"])
        textarea.send_keys(element["text"])

    button = browser.find_element_by_css_selector("#submit_button")
    button.click()
    print(browser._switch_to.alert.text)
finally:
    time.sleep(30)
    browser.quit()