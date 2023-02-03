import time
import math
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

result = ''

@pytest.fixture(scope="session")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    yield browser
    print("\nquit browser..")
    browser.quit()
    print(f"\n{result=}")
    with open(r'3_6\result.txt','w') as f:
        f.write(result)
    print("You can also find the result in the file result.txt")

@pytest.mark.parametrize('num', [236895, 236896, 236897, 236898, 236899, 236903, 236904, 236905])
def test_guest_should_see_owls(browser, num):
    link = f"https://stepik.org/lesson/{num}/step/1"
    browser.get(link)
    answer = math.log(int(time.time()))
    browser.find_element(By.TAG_NAME, "textarea").send_keys(answer)
    browser.find_element(By.CLASS_NAME, "submit-submission").click()
    response = browser.find_element(By.CLASS_NAME, "smart-hints__hint")
    feedback = response.text
    if feedback != 'Correct!':
        global result
        result += feedback

    assert feedback == 'Correct!'