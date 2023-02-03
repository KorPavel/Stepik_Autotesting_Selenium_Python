from selenium.webdriver.common.by import By

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    print('\n\t\tTEST#1 "Guest can go to login page"')
    browser.get(link)
    login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
    login_link.click()