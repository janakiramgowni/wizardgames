import pytest

from selenium.webdriver.common.by import By
from TESTS.Test_LOGINPAGE import BasePage

from PAGES.BASE_PAGE import BasePage
from CONFIG.CONFIG import TestData


class LoginPage(BasePage):
    EMAIL = (By.ID, "standard_user")
    PASSWORD = (By.ID, "secret_sauce")
    LOGIN_BUTTON = (By.ID, "login-button")

    """constructor of the page class"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASIC_URL)

    """this is used to login to app"""

    def do_login(self, USER_NAME, PASSWORD):
        self.do_send_keys(self.EMAIL, USER_NAME)
        self.do_send_keys(self.PASSWORD, PASSWORD)
        self.do_click(self.LOGIN_BUTTON)

    def failed_login(self, username, password):
         self.do_send_keys(self.WRONG_USER_NAME, username)
         self.do_send_keys(self.PASSWORD1, password)
         self.do_click(self.LOGIN_BUTTON)


