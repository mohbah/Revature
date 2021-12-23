from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class  NewReimbursement:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def select_amount_box(self):
        element: WebElement = self.driver.find_element(By.ID, "amount")
        return element

    def select_Type_box(self):
        element: WebElement = self.driver.find_element(By.ID, "type-selector")
        return element

    def select_submmit_button(self):
        element: WebElement = self.driver.find_element(By.ID, "create-reimb-btn")
        return element

