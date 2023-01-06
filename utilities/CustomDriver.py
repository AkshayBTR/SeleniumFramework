import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait



@pytest.mark.usefixtures("setup")
class CustomeDriver:

    def explicit_wait(self,condition,element=None,time=10):
        wait=WebDriverWait(self.driver,time)
        if element!=None:
            wait.until(condition(element))
        else:
            wait.until(condition())

    def getElement(self,by_class,locator_value):
        return self.driver.find_element(by_class,locator_value)

    def getElements(self,by_class,locator_value):
        return self.driver.find_elements(by_class,locator_value)

    def doClick(self,element):
        element.click()

    def selectElement(self,by_class,locator_value,select_type,element_value):
        options=Select(self.getElement(by_class,locator_value))
        if select_type.lower()=="index":
            options.select_by_index(element_value)
        elif select_type.lower()=="value":
            options.select_by_value(element_value)
        else:
            options.select_by_visible_text(element_value)

    def pushData(self,element,data):
        element.send_keys(data)