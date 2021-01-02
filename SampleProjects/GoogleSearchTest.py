from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import HtmlTestRunner

class GoogleSearch(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='../SeleniumTests/drivers/chromedriver')
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_search_myname(self):
        self.driver.get("https://google.com.tr")
        self.driver.find_element_by_name("q").send_keys("Alican Dartar")
        self.driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[3]/center/input[1]').click()

    def test_search_othername(self):
        self.driver.get("https://google.com.tr")
        self.driver.find_element_by_name("q").send_keys("Other Name Here")
        self.driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[3]/center/input[1]').click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='../SeleniumTests/reports'))






