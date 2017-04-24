import unittest
from selenium import webdriver
from cssdiner_webminion.pages import MainPage


class CssDinerLevels(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get('https://flukeout.github.io')
        self.page = MainPage(self.driver)

    def test_level_1(self):
        self.page.open_level(1)
        self.page.css_write("page")
        assert '2 of ' in self.page.level_text_span.get_attribute('innerHTML')

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
