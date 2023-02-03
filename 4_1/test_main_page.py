from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"

def go_to_login_page(browser):
    login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
    login_link.click()


def test_guest_can_go_to_login_page(browser):
    print('\n\t\tTEST#1 "Guest can go to login page"')
    browser.get(link)
    go_to_login_page(browser)