import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage

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
        self.driver.implicitly_wait(30)
        self.lp = LoginPage(self.driver)
        self.lp.clickLogin1()
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin2()
        act_title = self.driver.title
        self.driver.close()