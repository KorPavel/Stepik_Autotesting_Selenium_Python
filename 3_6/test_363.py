import pytest
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/{language}/"

@pytest.mark.parametrize('language', ["ru", "en-gb"])
def test_guest_should_see_login_link(browser, language):
    print('\n\t\tTEST#1 - "гость должен увидеть ссылку для входа"')
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#login_link")

