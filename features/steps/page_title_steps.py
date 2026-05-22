from behave import given, then

@given('user is on login page')
def step_impl(context):
    context.driver.get("https://the-internet.herokuapp.com/login")

@then('the page title should be displayed')
def step_impl(context):
    assert context.driver.title is not None