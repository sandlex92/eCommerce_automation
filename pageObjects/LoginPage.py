from selenium.webdriver.common.by import By
class LoginPage:
    #Login Page
    link_login1_xpath = "//a[@id='login2']"
    textbox_username_id = "loginusername"
    textbox_password_id = "loginpassword"
    button_login_xpath = "//button[contains(text(),'Log in')]"
    button_logout_id = "logout2"

#Defualt constructor for driver

    def __init__(self,driver):
        self.driver = driver
    #def clickLogin1(self):
        #self.driver.find_element(By.XPATH,self.link_login1_xpath).click()
    def setUserName(self,username):
        self.driver.find_element(By.ID,self.textbox_username_id).clear()
        self.driver.find_element(By.ID,self.textbox_username_id).send_keys(username)
    def setPassword(self,password):
        self.driver.find_element(By.ID,self.textbox_password_id).clear()
        self.driver.find_element(By.ID,self.textbox_password_id).send_keys(password)

    def clickLogin2(self):
        self.driver.find_element(By.XPATH,self.button_login_xpath).click()

    def Logout(self):
        self.driver.find_element(By.ID,self.button_logout_id).click()
