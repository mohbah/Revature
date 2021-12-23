from behave.runner import Context
from selenium import webdriver

from E2E_tests.page_object_models.approve import Approve
from E2E_tests.page_object_models.deny import Deny
from E2E_tests.page_object_models.employee_dashboard import EmployeeDashboard
from E2E_tests.page_object_models.newReimbursement import NewReimbursement
from page_object_models.login_page import LoginPage


def before_all(context:Context):
    context.driver = webdriver.Chrome(r"C:\Users\mohba\PycharmProjects\Project1\chromedriver.exe")
    context.lgnhome = LoginPage(context.driver)
    context.employeedashboard = EmployeeDashboard(context.driver)
    context.newreimbursement = NewReimbursement(context.driver)
    context.approve = Approve(context.driver)
    context.deny = Deny(context.driver)






def after_all(context:Context):
    context.driver.quit()