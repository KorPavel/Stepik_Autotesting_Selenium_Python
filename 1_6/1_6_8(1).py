from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import \
    presence_of_all_elements_located as elem_loc
from selenium.webdriver.support.expected_conditions import \
    element_to_be_clickable as elem_click


def get_answer(driver_browser):
    """
    Получаем решение
    :param driver_browser: webdriver
    :return: результат
    """
    browser.get("http://suninjuly.github.io/find_xpath_form")
    values = ('Ivan', 'Petrov', 'Smolensk', 'Russia')
    [elem.send_keys(values[num]) for num, elem in
     enumerate(browser.find_elements_by_tag_name("input"))]
    browser.find_element_by_xpath('//button[text()="Submit"]').click()
    alert = browser.switch_to.alert
    result = alert.text.split()[-1]
    alert.accept()
    return result


def wait_spinner(driver_browser):
    """
    Ждём, пока спиннер пропадёт
    :param driver_browser: webdriver
    :return: None
    """
    driver_wait = WebDriverWait(driver_browser, 9)
    for class_name in ('loader__spinner', 'stepik-loader'):
        driver_wait.until_not(elem_loc((By.CLASS_NAME, class_name)))
    for txt in ('подождите, не покидайте страницу',
                'С этого шага можно безопасно уходить'):
        driver_wait.until_not(elem_loc((By.XPATH,
                                        f'//span[contains(text(),{txt})]')))


try:
    browser = webdriver.Chrome()

    # получаем решение
    answer = get_answer(browser)
    print(answer)

    # идем на страницу авторизации степика
    browser.get('https://stepik.org/catalog?auth=login')
    wait = WebDriverWait(browser, 9)
    submit = wait.until(elem_click((By.CLASS_NAME,
                                    'sign-form__btn.button_with-loader')))
    # логинимся на сайт
    browser.find_element(By.NAME, 'login').send_keys('your_login')
    browser.find_element(By.NAME, 'password').send_keys('your_password')
    submit.click()
    wait.until(elem_click((By.CLASS_NAME, 'navbar__profile-img')))
    # идем на страницу урока
    browser.get('https://stepik.org/lesson/138920/step/8?unit=196194')
    wait_spinner(browser)
    # если есть решение - обновим
    if browser.find_elements(By.CLASS_NAME, 'again-btn'):
        browser.find_element(By.CLASS_NAME, 'again-btn').click()
        if browser.find_elements(By.CLASS_NAME, 'modal-popup__container'):
            # подтвердим, что хотим решить снова
            browser.find_element_by_xpath('//button[text()="OK"]').click()
            # очистим поле "решение"
            wait.until(elem_click((By.TAG_NAME, "textarea"))).clear()
    # вставка ответа
    wait.until(elem_click((By.TAG_NAME, "textarea"))).send_keys(answer)
    # отправка решения
    browser.find_element(By.CLASS_NAME, 'submit-submission').click()
    wait_spinner(browser)
    if browser.find_elements(By.CLASS_NAME, 'attempt-message_wrong'):
        print('Неверное решение!!!')
        # что-то пошло не так подержим браузер 30 сек
        __import__('time').sleep(30)
    else:
        print('Решено верно!!!')

finally:
    browser.quit()