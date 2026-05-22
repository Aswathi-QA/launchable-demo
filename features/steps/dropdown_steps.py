from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

@given('user is on dropdown page')
def step_impl(context):
    context.driver.get("https://the-internet.herokuapp.com/dropdown")

@when('user selects option two')
def step_impl(context):
    dropdown = Select(context.driver.find_element(By.ID, "dropdown"))
    dropdown.select_by_visible_text("Option 2")

@then('option two should be selected')
def step_impl(context):
    selected = context.driver.find_element(By.CSS_SELECTOR, "#dropdown option:checked").text
    assert selected == "Option 2"
   