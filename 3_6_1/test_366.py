from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"


def test_guest_should_see_login_link(browser):
    print('\n\t\tTEST-Login link')
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#login_link")
    assert True