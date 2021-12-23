from behave import Given,When,Then
import time

@Given(u'The employee user is on the employee dashboard')
def step_impl(context):
    context.driver.get(r"http://127.0.0.1:4000/employee_dashboard.html")


@When(u'the employee clicks on the new riembursement button')
def step_impl(context):
    context.employeedashboard.select_new_riembursement_button().click()


@Then(u'The employee should be redirected to the new riembursement page')
def step_impl(context):
    time.sleep(1)
    assert context.driver.title == "Create New Reimbursement"
