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

    button1 = browser.find_element(By.ID, 'robotCheckbox').click()

    # Определяем "button2" и прокручиваем его до видимости, далее кликаем на неё.
    button2 = browser.find_element(By.ID, 'robotsRule')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button2)
    button2.click()
    button3 = browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    print_answer(browser)
finally:
    browser.quit()