import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class Test_001_Login:
    baseURL = "https://www.demoblaze.com/index.html"
    username = "testuser_92@gmail.com"
    password = "admin"

    def test_homePageTitle(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        self.driver.close()
        if act_title == "STORE":
            assert True
        else:
            assert False

    def test_login(self,setup):
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        main_page = setup.current_window_handle
        sleep(5)
        setup.find_element(By.XPATH,"//body[1]/nav[1]/div[1]/ul[1]/li[5]/a[1]").click()
        sleep(5)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin2()
        act_title = self.driver.title
        self.driver.close()