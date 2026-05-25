from selenium import webdriver
from selenium.webdriver.firefox.options import Options

def before_scenario(context, scenario):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # Reduce Firefox internal logging (safe)
    options.log.level = "fatal"

    context.driver = webdriver.Firefox(options=options)

def after_scenario(context, scenario):
    if hasattr(context, "driver"):
        try:
            context.driver.quit()
        except:
            pass
