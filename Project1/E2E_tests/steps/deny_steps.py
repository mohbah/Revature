import time

from behave import Given, When, Then
from selenium.webdriver.common.alert import Alert


@Given(u'The managerr  is on the manager dashboard')
def step_impl(context):
    context.driver.get(r"http://127.0.0.1:4000/manager_dashboard.html")


@When(u'the managerr enters reimbursement id {id} into the reimbursmeent id box')
def step_impl(context, id:str):
    context.deny.select_id_box().send_keys(id)


@When(u'the managerr enters his commentt {comment} into the manager comment box')
def step_impl(context, comment : str):
    context.deny.select_comment_box().send_keys(comment)


@When(u'the managerr clicks on the new deny button')
def step_impl(context):
    context.driver.execute_script('arguments[0].click()', context.deny.select_deny_button())


@Then(u'The managerr should be redirected to the manager dashboard')
def step_impl(context):
    alert = Alert(context.driver)
    time.sleep(1)
    assert alert.text == "successfully Denied!"
