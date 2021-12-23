from behave import Given,When,Then
import time

@Given(u'The employee user is on the log-in page')
def step_impl(context):
    context.driver.get(r"http://127.0.0.1:4000/index.html")

@When(u'The employee user inputs {value} into the username bar')
def step_impl(context, value : str):
    context.lgnhome.select_username_box().send_keys(value)


@When(u'The employee user inputs {value} into the password bar')
def step_impl(context, value : str):
    context.lgnhome.select_password_box().send_keys(value)


@When(u'the employee clicks on the log-in button')
def step_impl(context):
   context.lgnhome.select_login_button().click()


@Then(u'The employee should be redirected to the Dashboard page with the title {title}')
def step_impl(context, title: str):
    time.sleep(1)
    assert context.driver.title == title




#@When(u'The manager user inputs David into the username bar')
#def step_impl(context):
 #   raise NotImplementedError(u'STEP: When The manager user inputs David into the username bar')


#@When(u'The manager user inputs Beckham into the password bar')
#def step_impl(context):
 #   raise NotImplementedError(u'STEP: When The manager user inputs Beckham into the password bar')


#@When(u'the manager clicks on the log-in button')
#def step_impl(context):
 #   raise NotImplementedError(u'STEP: When the manager clicks on the log-in button')


#@Then(u'The manager should be redirected to the Dashboard page with the title Manager Reimbursement Dashboard')
#def step_impl(context):
 #   raise NotImplementedError(u'STEP: Then The manager should be redirected to the Dashboard page with the title Manager Reimbursement Dashboard')
