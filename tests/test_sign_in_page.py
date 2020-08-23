from tests.base_test import BaseTest
from pages.main_page import MainPage
#https://github.com/smirad91/SeleniumCursor

class TestSignInPage(BaseTest):


    def test_sign_in_with_in_valid_user(self):
        main_page = MainPage(self.driver)
        login_page = main_page.login_click()
        result = login_page.login()