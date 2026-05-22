from behave import given, then

@then('the page title should be displayed')
def step_impl(context):
    assert context.driver.title is not None