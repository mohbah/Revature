from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

class  EmployeeDashboard:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def select_new_riembursement_button(self):
        element: WebElement = self.driver.find_element(By.ID, "new-reimb-btn")
        return element
