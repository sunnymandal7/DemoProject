from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from Utils.browserutils import browserutils

class LoginPage(browserutils):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.username = (By.XPATH, "//input[@id='username']")
        self.Password = (By.XPATH, "//input[@id='password']")
        self.dropdown = (By.XPATH, "//select[@class='form-control']")
        self.login_checkbox = (By.XPATH, "//input[@id='terms']")
        self.Login_Submit = (By.XPATH, "//input[@type='submit']")

    def Login(self, username, password):
        self.driver.find_element(*self.username).send_keys(username)
        self.driver.find_element(*self.Password).send_keys(password)
        dropdown = self.driver.find_element(*self.dropdown)
        select = Select(dropdown)
        select.select_by_visible_text("Student")
        self.driver.find_element(*self.login_checkbox).click()
        self.driver.find_element(*self.Login_Submit).click()
