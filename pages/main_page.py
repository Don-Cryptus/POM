from pages.base_page import BasePage
from pages.login_page import LoginPage
from utils import users
from utils.locators import *



class MainPage(BasePage):
    def __init__(self, driver):
        print("user_page __init__")
        self.locator = MainPageLocators
        self.user = users.get_user("google")
        super().__init__(driver)  # Python3 version

    def change_language(self):
        self.hover(*self.locator.LANGUAGE)
        self.switch_to_iframe()
        self.hover(*self.locator.ENGLISH)

    def check_page_loaded(self):
        return True if self.find_element(*self.locator.LOGO) else False

    def click_sign_in_button(self):
        self.hover(*self.locator.LOGIN)

    def click_facebook_login_button(self):
        self.hover(*self.locator.FACEBOOK_LOGIN)

    def click_google_login_button(self):
        self.hover(*self.locator.GOOGLE_LOGIN)

    def click_apple_login_button(self):
        self.hover(*self.locator.APPPLE_LOGIN)

    def switch_to_iframe(self):
        self.iframe = self.find_element(*self.locator.IFRAME)
        self.iframe2 = self.switch_iframe(self.iframe)

    def login_click(self):
        # self.change_language()
        self.click_sign_in_button()
        self.switch_to_iframe()

        #self.google_login_button = self.check_element(*self.locator.GOOGLE_LOGIN)
        if self.user["provider"] == "google":
            self.click_google_login_button()
        elif self.user["provider"] == "facebook":
            self.click_facebook_login_button()
        elif self.user["provider"] == "apple":
            self.click_apple_login_button()

        if self.check_element(*self.locator.VALIDATION_CONTINUE):
            LoginPage(self.driver, self.user).age_gender_verification()
        else:
            return LoginPage(self.driver, self.user)

