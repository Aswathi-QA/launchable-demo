from behave import given, when, then
from selenium.webdriver.common.by import By

@given('user is on checkbox page')
def step_impl(context):
    context.driver.get("https://the-internet.herokuapp.com/checkboxes")

@when('user selects checkbox one')
def step_impl(context):
    checkbox = context.driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")[0]
    checkbox.click()

@then('checkbox one should be selected')
def step_impl(context):
    checkbox = context.driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")[0]
    assert checkbox.is_selected()
   