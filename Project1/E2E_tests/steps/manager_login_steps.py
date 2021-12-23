from behave import Given,When,Then
import time


@Given(u'The manager user is on the log-in page')
def step_impl(context):
    context.driver.get(r"http://127.0.0.1:4000/index.html")


@When(u'The manager user inputs {value} into the username bar')
def step_impl(context, value: str):
    context.lgnhome.select_manager_username_box().send_keys(value)


@When(u'The manager user inputs {value} into the password bar')
def step_impl(context, value: str):
   context.lgnhome.select_manager_password_box().send_keys(value)


@When(u'the manager clicks on the log-in button')
def step_impl(context):
    context.lgnhome.select_manager_login_button().click()


@Then(u'The manager should be redirected to the Dashboard page with the title {title}')
def step_impl(context, title:str):
    time.sleep(1)
    assert context.driver.title == title
