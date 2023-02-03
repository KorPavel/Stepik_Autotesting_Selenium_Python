import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# ссылка на сайт
link = 'http://suninjuly.github.io/simple_form_find_task.html'
# данные для ввода
values = [
    'Ivan',
    'Petrov',
    'Smolensk',
    'Russia'
]
# список полей ввода
inputs = [0]
# запускаем вебдравер хром
browser = webdriver.Chrome()
# пробуем
try:
    # открываем окно хрома по ссылке
    browser.get(link)
    # ищем поля по селектору и заполняем данными из values
    for number in range(1, len(values)+1):
        inputs.append(browser.find_element(By.CSS_SELECTOR, f'.form-group:nth-child({number}) input'))
        inputs[number].send_keys(values[number-1])
        print(f'{number} поле: {values[number-1]}')

    # ищем кнопку submit
    submit_button = browser.find_element(By.ID, "submit_button")
    # нажимаем кнопку submit
    submit_button.click()
    print(browser._switch_to.alert.text)
finally:
    # пауза
    time.sleep(30)
    # закрываем все процессы драйвера
    browser.quit()