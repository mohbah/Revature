from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

class  Approve:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def select_id_box(self):
            element: WebElement = self.driver.find_element(By.ID, "reimb-resolve-input")
            return element

    def select_comment_box(self):
            element: WebElement = self.driver.find_element(By.ID, "reimb-resolve-comment")
            return element

    def select_approve_button(self):
        element: WebElement = self.driver.find_element(By.ID, "approve-reimb")
        return element

