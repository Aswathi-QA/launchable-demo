from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

@given('user is on login page')
def step_impl(context):
    options = Options()
    options.add_argument("--headless")

    # ✅ Selenium Manager handles geckodriver
    context.driver = webdriver.Firefox(options=options)
    context.driver.get("https://the-internet.herokuapp.com/login")

@when('user enters valid username and password')
def step_impl(context):
    context.driver.find_element(By.ID, "username").send_keys("tomsmith")
    context.driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    context.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

@then('user should see secure area')
def step_impl(context):
    assert "secure" in context.driver.current_url.lower()
    context.driver.quit()

@when('user enters invalid username and password')
def step_impl(context):
    context.driver.find_element(By.ID, "username").send_keys("wrong")
    context.driver.find_element(By.ID, "password").send_keys("wrong")
    context.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

@then('user should see error message')
def step_impl(context):
    error = context.driver.find_element(By.ID, "flash").text
    assert "invalid" in error.lower()
    context.driver.quit()