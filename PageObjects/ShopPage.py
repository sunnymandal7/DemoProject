import time

from selenium.webdriver.common.by import By

from Utils.browserutils import browserutils


class ShopPage(browserutils):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
        self.driver.implicitly_wait(10)
        self.shop_button = (By.XPATH, "//a[contains(text(),'Shop')]")
        self.all_Products = (By.XPATH, "//div[@class='card h-100']")

    def Add_Product_to_Cart(self,product_name):
        time.sleep(10)
        # self.capture_step("User logged in successfully and navigated to home page")
        self.driver.find_element(*self.shop_button ).click()
        time.sleep(5)
        products = self.driver.find_elements(*self.all_Products)
        for product in products:
            name = product.find_element(By.XPATH, "//div//h4//a").text
            if name == product_name:
                product.find_element(By.XPATH, "/div/button/div/button").click()