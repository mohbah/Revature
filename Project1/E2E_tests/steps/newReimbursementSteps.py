import time

from behave import Given,When,Then
from selenium.webdriver.common.alert import Alert


@Given(u'The employee user is on the new riembursement page')
def step_impl(context):
    context.driver.get(r"http://127.0.0.1:4000/new-reimbursement.html")


@When(u'the employee entered the reimbursement amount {amount}')
def step_impl(context, amount : str):
    context.newreimbursement.select_amount_box().send_keys(amount)



@When(u'the employee have chosed the reimbursement type {type}')
def step_impl(context, type:str):
    context.newreimbursement.select_Type_box().send_keys(type)


@When(u'the employee clicks on the submmit new riembursement button')
def step_impl(context):
    context.newreimbursement.select_submmit_button().click()



@Then(u'The employee should recieve an Alert')
def step_impl(context):
    alert = Alert(context.driver)
    time.sleep(1)
    assert alert.text == "Successfully Submitted!"



