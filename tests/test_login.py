import time

import pytest
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage
from pages.welcome_page import WelcomePage
from utilities.CustomDriver import CustomeDriver


class Test_Login(CustomeDriver):
    def test_login_feature(self):
        #creating an object of welcome page and getting login element from it
        welcomepage=WelcomePage(self.driver)
        welcomepage.get_login_button().click()

        #creating an object of login page and getting create user element from it
        loginpage=LoginPage(self.driver)
        loginpage.get_create_button().click()

        #creating an object of register page and getting elements from it
        registerpage=RegistrationPage(self.driver)
        self.pushData(registerpage.get_First_name(),"akshay")
        self.pushData(registerpage.get_Last_name(),"kumar")
        registerpage.get_gender("female")
        self.pushData(registerpage.get_Phone_Number(),"9123123123")
        self.pushData(registerpage.get_Email(),"akshay@gmail.com")
        self.pushData(registerpage.get_Password(),"Avk@12345")
        self.pushData(registerpage.get_confirm_pwd(),"Avk@12345")
        self.doClick(registerpage.get_aggreement())
        self.explicit_wait(EC.element_to_be_clickable,registerpage.get_register(),10)
        self.doClick(registerpage.get_register())