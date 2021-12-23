import time

from behave import Given, When, Then
from selenium.webdriver.common.alert import Alert


@Given(u'The manager user is on the manager dashboard')
def step_impl(context):
    context.driver.get(r"http://127.0.0.1:4000/manager_dashboard.html")


@When(u'the manager enter reimbursement id {id} into the reimbursmeent id box')
def step_impl(context, id: str):
    context.approve.select_id_box().send_keys(id)


@When(u'the manager enters his comment {comment} into the manager comment box')
def step_impl(context, comment: str):
    context.approve.select_comment_box().send_keys(comment)


@When(u'the manager clicks on the new approve button')
def step_impl(context):
    context.driver.execute_script('arguments[0].click()', context.approve.select_approve_button())


@Then(u'The manager should be redirected to the manager dashboard')
def step_impl(context):
    alert = Alert(context.driver)
    time.sleep(1)
    assert alert.text == "successfully Approved!"


