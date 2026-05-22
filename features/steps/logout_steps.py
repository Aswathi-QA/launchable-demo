from behave import given, when, then
from selenium.webdriver.common.by import By

@given('user is logged in')
def step_impl(context):
    context.execute_steps("""
        Given user is on login page
        When user enters valid username and password
    """)

@when('user clicks logout')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, "a.button").click()

@then('user should be redirected to login page')
def step_impl(context):
    assert "login" in context.driver.current_url
    context.driver.quit()