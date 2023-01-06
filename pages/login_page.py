from selenium.webdriver.common.by import By

from utilities.CustomDriver import CustomeDriver


class LoginPage(CustomeDriver):
    Create_Button_ID="fl_create_account"
    def __init__(self,driver):
        self.driver=driver

    def get_create_button(self):
        return self.getElement(By.ID,self.Create_Button_ID)