from selenium.webdriver.common.by import By


# for maintainability we can seperate web objects by page name


class FacebookLoginPageLocators(object):
    EMAIL = (By.XPATH,'//*[@name="email"]')
    CONTINUE = ('')
    PASSWORD = (By.XPATH,'//*[@name="pass"]')
    SUBMIT = (By.XPATH,'//*[@name="login"]')
    ERROR_MESSAGE = (By.ID,'message_error')
    IFRAME = (By.XPATH,'//*[contains(@class, "webAuthContainer__iframe")]')
    AGE = (By.XPATH,'//*[@name="age"]')
    GENDER_SELECT = (By.XPATH,'//*[@name="gender"]')
    GENDER_MALE = (By.XPATH,'//select[@name="gender"]/option[@value="male"]')
    GENDER_FEMALE = (By.XPATH,'//select[@name="gender"]/option[@value="female"]')
    VALIDATION_CONTINUE = (By.XPATH,'//*[@id="submit_signup"]')
    VALIDATION_ERROR = (By.XPATH,'//*[@class="validation-error"]')
    VALIDATION_CLOSE = (By.XPATH,'//*[@title="Close"]')


class GoogleLoginPageLocators(object):
    EMAIL = (By.XPATH,'//*[@type="email"]')
    CONTINUE = (By.XPATH,'//*[@id="identifierNext"]')
    PASSWORD = (By.XPATH,'//*[@type="password"]')
    SUBMIT = (By.XPATH,'//*[@id="passwordNext"]')
    ERROR_MESSAGE = (By.ID,'message_error')
    IFRAME = (By.XPATH,'//*[contains(@class, "webAuthContainer__iframe")]')
    AGE = (By.XPATH,'//*[@name="age"]')
    GENDER_SELECT = (By.XPATH,'//*[@name="gender"]')
    GENDER_MALE = (By.XPATH,'//select[@name="gender"]/option[@value="male"]')
    GENDER_FEMALE = (By.XPATH,'//select[@name="gender"]/option[@value="female"]')
    VALIDATION_CONTINUE = (By.XPATH,'//*[@id="submit_signup"]')
    VALIDATION_ERROR = (By.XPATH,'//*[@class="validation-error"]')
    VALIDATION_CLOSE = (By.XPATH,'//*[@title="Close"]')


class AppleLoginPageLocators(object):
    EMAIL = (By.XPATH,'//*[@type="text"]')
    CONTINUE = ''
    PASSWORD = (By.XPATH,"//*[@name='pass']")
    SUBMIT = (By.XPATH,"//*[@name='login']")
    ERROR_MESSAGE = (By.ID,'message_error')
    IFRAME = (By.XPATH,'//*[contains(@class, "webAuthContainer__iframe")]')
    AGE = (By.XPATH,'//*[@name="age"]')
    GENDER_SELECT = (By.XPATH,'//*[@name="gender"]')
    GENDER_MALE = (By.XPATH,'//select[@name="gender"]/option[@value="male"]')
    GENDER_FEMALE = (By.XPATH,'//select[@name="gender"]/option[@value="female"]')
    VALIDATION_CONTINUE = (By.XPATH,'//*[@id="submit_signup"]')
    VALIDATION_ERROR = (By.XPATH,'//*[@class="validation-error"]')
    VALIDATION_CLOSE = (By.XPATH,'//*[@title="Close"]')


class MainPageLocators(object):
    LOGO = (By.XPATH,"//*[contains(@class, 'header__logoLink-wordmark')]")
    LOGIN = (By.XPATH,"//*[contains(@class, 'loginButton')]")
    IFRAME = (By.XPATH,"//iframe")
    FACEBOOK_LOGIN = (By.XPATH,"//*[contains(@class, 'sc-button-facebook')]")
    GOOGLE_LOGIN = (By.XPATH,"//*[contains(@class, 'sc-button-google')]")
    APPLE_LOGIN = (By.XPATH,"//*[contains(@class, 'sc-button-apple')]")
    VALIDATION_CONTINUE = (By.XPATH, '//*[@id="submit_signup"]')
    LANGUAGE = (By.XPATH,'//*[contains(@class, "localeSelector") and contains(@class, "sc-pointer")]')
    #LANGUAGE = (By.XPATH,'//*[@aria-haspopup="true"]')
    ENGLISH = (By.XPATH,'//*[@data-locale="en"]')
