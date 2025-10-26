from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Utils.browserutils import browserutils


class CheckOutPage(browserutils):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.header_checkout = (By.XPATH, "//a[contains(text(),'Checkout')]")
        self.final_checkout = (By.XPATH, "//button[contains(text(),'Checkout')]")
        self.findCountry = (By.XPATH, "//input[@id='country']")
        self.checkbox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
        self.submit = (By.XPATH, "//input[@type='submit']")

    def Product_Checkout(self):
        self.driver.find_element(*self.header_checkout).click()
        self.driver.find_element(*self.final_checkout).click()
        self.driver.find_element(*self.findCountry).send_keys("IND")
        wait = WebDriverWait(self.driver, 5)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
        self.driver.find_element(By.LINK_TEXT, "India").click()
        self.driver.find_element(*self.checkbox).click()
        self.driver.find_element(*self.submit).click()

    def ValidateSuccessMessage(self):
        Result = self.driver.find_element(By.CLASS_NAME, "alert-success").text
        assert "Success! " in Result