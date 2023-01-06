from selenium.webdriver.common.by import By

from utilities.CustomDriver import CustomeDriver

class WelcomePage(CustomeDriver):
    Login_Button_ID="fl_login_btnw"
    def __init__(self,driver):
        self.driver=driver

    def get_login_button(self):
        return self.getElement(By.ID,self.Login_Button_ID)