from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

#проверяем значение атрибута checked у people_radio
    people_radio = browser.find_element(By.ID, "peopleRule")
    people_checked = people_radio.get_attribute("checked")
    print("value 'checked' of people radio: ", people_checked)
    assert people_checked == "true", "People radio is not selected by default"

#проверяем значение атрибута checked у robots_radio
    robots_radio = browser.find_element(By.ID, "robotsRule")
    robots_checked = robots_radio.get_attribute("checked")
    print("value 'checked' of robots_radio: ", robots_checked)
    assert robots_checked is None, "Robots radio is not selected by default"

#проверяем значение атрибута disabled у кнопки Submit
    button = browser.find_element(By.CSS_SELECTOR, '.btn')
    button_disabled = button.get_attribute("disabled")
    print("value 'disabled' of button Submit befor 10 sec: ", button_disabled)
    assert button_disabled is None, "Button disabled is not selected by default"

#проверяем значение атрибута disabled у кнопки Submit после таймаута
    time.sleep(10)
    button_disabled = button.get_attribute("disabled")
    print("value 'disabled' of button Submit after 10sec: ", button_disabled)
    assert button_disabled == "true", "People radio is not selected by default"

finally:
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла