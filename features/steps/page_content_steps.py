from behave import given, then
from selenium.webdriver.common.by import By

@given('user is on the home page')
def step_impl(context):
    context.driver.get("https://the-internet.herokuapp.com")

@then('the page heading should be displayed')
def step_impl(context):
    heading = context.driver.find_element(By.TAG_NAME, "h1")
    assert heading.is_displayed()
    assert heading.text == "Welcome to the-internet"