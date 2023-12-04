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
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        wait = WebDriverWait(self.driver, 10)
        wait.until((EC.element_to_be_clickable(By.XPATH,"//a[@id='login2']"))).click()

        #sleep(10)
        #self.lp.clickLogin1()
        # main_page = self.driver.current_window_handle
        # sleep(5)
        # self.lp = LoginPage(self.driver)
        # sleep(5)
        # self.lp.clickLogin1()
        # for handle in self.driver.window_handles:
        #     if handle != main_page:
        #         login_page = handle
        # self.driver.switch_to.window(login_page)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin2()
        act_title = self.driver.title
        self.driver.close()