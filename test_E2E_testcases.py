import json

import pytest

from PageObjects.CheckOutPage import CheckOutPage
from PageObjects.LoginPage import LoginPage
from PageObjects.ShopPage import ShopPage
# pytest --env staging --BrowserName chrome
test_data_path = 'TestData/active_user.json'
with open(test_data_path) as json_file:
    test_data = json.load(json_file)
    test_list = test_data["active_user"]
    test_list1 = test_data["Inactive_user"]

@pytest.mark.parametrize("TestDataItem",test_list)
def test_validate_successful_checkout(browser_instance,TestDataItem):
    driver = browser_instance
    driver.maximize_window()
    loginPage = LoginPage(driver)
    print(loginPage.gettitle())
    loginPage.Login(TestDataItem["userEmail"], TestDataItem["userPassword"])
    shop_page = ShopPage(driver)
    shop_page.Add_Product_to_Cart("Blackberry")
    checkout = CheckOutPage(driver)
    checkout.Product_Checkout()
    checkout.ValidateSuccessMessage()

@pytest.mark.parametrize("TestDataItem",test_list1)
def test_validate_invalid_user_login(browser_instance,TestDataItem):
    driver = browser_instance
    driver.maximize_window()
    loginPage = LoginPage(driver)
    print(loginPage.gettitle())
    loginPage.Login(TestDataItem["userEmail"], TestDataItem["userPassword"])
