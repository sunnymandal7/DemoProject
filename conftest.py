import os
from pickle import GLOBAL

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import datetime
driver = None

def pytest_addoption(parser):
    parser.addoption(
        "--BrowserName", action="store", default="chrome", help="Browser Selection"
    )
@pytest.fixture(scope = "function")
def browser_instance(request):
    global driver
    BrowserName = request.config.getoption("BrowserName")
    service_obj = Service()
    if BrowserName == "chrome":
        driver = webdriver.Chrome(service=service_obj)
    elif BrowserName == "Edge":
        driver = webdriver.Edge(service=service_obj)
    driver.implicitly_wait(5)
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    yield driver
    driver.close()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Hook to capture screenshot on test failure.
    Works for both pytest-html and Allure reports.
    """
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("browser_instance")
        if driver:
            # Create screenshots folder if missing
            os.makedirs("./Reports/screenshots", exist_ok=True)

            # File name with timestamp
            file_name = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
            capture_path = f"./Reports/screenshots/{file_name}.png"

            # Save screenshot
            driver.save_screenshot(capture_path)
            print(f"Screenshot saved at {capture_path}")

        else:
            print("No WebDriver instance found for screenshot.")

def Get_screenshot(filename):
    driver.get_screenshot_as_file(filename)

