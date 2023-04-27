import pytest
from selenium.webdriver.common.by import By
from PAGES.BASE_PAGE import BasePage
from CONFIG.CONFIG import TestData
from selenium.webdriver.common.by import By


class Test_Login(BasePage):

    def test_login(self):
        self.LOGIN_PAGE = self.LOGIN_PAGE(self.driver)
        self.LOGIN_PAGE.do_login(TestData.USER_NAME, TestData.PASSWORD)

    def test_failed_login(self):
        self.LOGIN_PAGE = self.LOGIN_PAGE(self.driver)
        self.LOGIN_PAGE.do_login(TestData.WRONG_USER_NAME, TestData.PASSWORD1)
        assert self.LOGIN_PAGE.get_error_message() == """"Sorry, this user has been banned"""

    def test_order_product(self):
        self.LOGIN_PAGE = self.LOGIN_PAGE(self.driver)
        self.LOGIN_PAGE.do_login(TestData.USER_NAME, TestData.PASSWORD)



