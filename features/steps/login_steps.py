from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

@given('user is on login page')
def step_impl(context):
    service = Service(ChromeDriverManager().install())

    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    context.driver = webdriver.Chrome(service=service, options=options)
    context.driver.get("https://the-internet.herokuapp.com/login")
