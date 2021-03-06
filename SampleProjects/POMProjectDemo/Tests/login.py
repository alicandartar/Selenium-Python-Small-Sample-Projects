from selenium import webdriver
import time
import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from SampleProjects.POMProjectDemo.Pages.loginPage import LoginPage
from SampleProjects.POMProjectDemo.Pages.homePage import HomePage
import HtmlTestRunner

class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="../SeleniumTests/drivers/chromedriver")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_01login_valid(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")

        login = LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()

        homepage = HomePage(driver)
        homepage.click_welcome()
        homepage.click_logout()

        time.sleep(2)

    def test_02login_invalid_username(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")

        login = LoginPage(driver)
        login.enter_username("Admin1")
        login.enter_password("admin123")
        login.click_login()
        message = driver.find_element_by_id("spanMessage").text
        self.assertEqual(message, "Invalid credentials")

        time.sleep(2)
    
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("Test Completed")

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='../SeleniumTests/reports'))

