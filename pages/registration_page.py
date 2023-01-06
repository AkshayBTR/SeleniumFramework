from selenium.webdriver.common.by import By

from utilities.CustomDriver import CustomeDriver


class RegistrationPage(CustomeDriver):
    First_Name_ID="fl_firstName_Shopper"
    Last_Name_ID="fl_lastName_Shopper"
    Gender_XPATH="//input[@type='radio']"
    Phone_Number_ID="fl_phoneNumber_Shopper"
    Email_ID="fl_email_Shopper"
    Password_ID="fl_password_Shopper"
    Confirm_Password_ID="fl_confirmPassword_Shopper"
    Agree_Button_ID="fl_tc_Shopper"
    Register_Button_XPATH="//button[text()='Register']"
    def __init__(self,driver):
        self.driver=driver
    def get_First_name(self):
        return self.getElement(By.ID, self.First_Name_ID)
    def get_Last_name(self):
        return self.getElement(By.ID,self.Last_Name_ID)
    def get_genders(self):
        return self.getElements(By.XPATH,self.Gender_XPATH)
    def get_gender(self,gender_val):
        genders=self.get_genders()
        for gender in genders:
            if gender.text.lower() == gender_val.lower():
                return gender
    def get_Phone_Number(self):
        return self.getElement(By.ID, self.Phone_Number_ID)
    def get_Email(self):
        return self.getElement(By.ID,self.Email_ID)
    def get_Password(self):
        return self.getElement(By.ID, self.Password_ID)
    def get_confirm_pwd(self):
        return self.getElement(By.ID,self.Confirm_Password_ID)
    def get_aggreement(self):
        return self.getElement(By.ID, self.Agree_Button_ID)
    def get_register(self):
        return self.getElement(By.XPATH, self.Register_Button_XPATH)\
