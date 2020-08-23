import time

from utils.locators import *
from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, driver, user):
        self.user = user
        if self.user["provider"] == "google":
            self.locator = GoogleLoginPageLocators
        elif self.user["provider"] == "facebook":
            self.locator = FacebookLoginPageLocators
        elif self.user["provider"] == "apple":
            self.locator = AppleLoginPageLocators

        super().__init__(driver)

    def enter_email(self, email):
        self.find_element(*self.locator.EMAIL).send_keys(email)

    def enter_password(self, password):
        self.find_element(*self.locator.PASSWORD).send_keys(password)

    def click_login_button(self):
        self.hover(*self.locator.SUBMIT)

    def click_continue_button(self):
        self.hover(*self.locator.CONTINUE)

    def switch_window(self, x):
        self.driver.switch_to.window(self.driver.window_handles[x])

    def login(self):
        if self.user["provider"] == "google":
            self.login_google()
        elif self.user["provider"] == "facebook":
            self.login_facebook()
        elif self.user["provider"] == "apple":
            self.login_apple()

        if self.check_element(*self.locator.IFRAME):
            self.age_gender_verification()
        else:
            print("wtf")

    def enter_gender(self):
        self.hover(*self.locator.GENDER_SELECT)
        if self.user["gender"] == "male":
            self.find_element(*self.locator.GENDER_MALE).click()
        else:
            self.find_element(*self.locator.GENDER_FEMALE).click()

    def age_gender_verification(self):
        #change frame for verification
        if not self.check_element(*self.locator.VALIDATION_CONTINUE):
            self.iframe = self.find_element(*self.locator.IFRAME)
            self.switch_iframe(self.iframe)

        #enter age
        self.find_element(*self.locator.AGE).send_keys(self.user["age"])

        #enter gender
        self.enter_gender()

        #Click Validation Continue
        self.hover(*self.locator.VALIDATION_CONTINUE)

        #If error then restart the login proccess
        if self.check_element(*self.locator.VALIDATION_ERROR):
            from pages.main_page import MainPage
            #switch back from iframe
            self.driver.switch_to.default_content()
            #click close
            self.hover(*self.locator.VALIDATION_CLOSE)
            #relogin
            MainPage(self.driver).login_click()
        else:
            time.sleep(1000)
            print("fail")


    def login_facebook(self):
        self.switch_window(1)
        print(self.user)
        self.enter_email(self.user["email"])
        self.enter_password(self.user["password"])
        self.click_login_button()
        self.switch_window(0)

    def login_google(self):
        self.switch_window(1)
        print(self.user)
        self.enter_email(self.user["email"])
        self.click_continue_button()
        time.sleep(1)
        self.enter_password(self.user["password"])
        self.click_login_button()
        self.switch_window(0)

    def login_apple(self):
        self.switch_window(1)
        print(self.user)
        self.enter_email(self.user["email"])
        self.enter_password(self.user["password"])
        self.click_login_button()
        self.switch_window(0)


