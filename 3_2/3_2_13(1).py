from selenium import webdriver
import unittest

class TestRegistration(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(1)

    @classmethod
    def tearDownClass(self):
        self.browser.quit()

    def registration(self, link):
        self.browser.get(link)
        fields = self.browser.find_element_by_css_selector('.first_block .first_class input')
        fields.send_keys("Ivan")
        fields = self.browser.find_element_by_css_selector('.first_block .second_class input')
        fields.send_keys("Ivan")
        fields = self.browser.find_element_by_css_selector('.first_block .third_class input')
        fields.send_keys("Ivan")
        button = self.browser.find_element_by_xpath("//button[text()='Submit']")
        button.click()
        return self.browser.find_element_by_tag_name("h1").text

    def test_for_refistr(self):
        link = "http://suninjuly.github.io/registration1.html"
        self.assertEqual(self.registration(link), "Congratulations! You have successfully registered!", "ERROR")

    def test_for_refistr1(self):
        link = "http://suninjuly.github.io/registration2.html"
        self.assertEqual(self.registration(link), "Congratulations! You have successfully registered!", "ERROR")


if __name__ == "__main__":
    unittest.main()