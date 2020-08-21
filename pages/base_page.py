import time

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException,NoSuchElementException
import random
import decimal

# this Base class is serving basic attributes for every single page inherited from Page class
from utils import users


class BasePage(object):
    def __init__(self, driver, base_url='https://soundcloud.com/'):
        print("base_page __init__")
        self.base_url = base_url
        self.driver = driver
        #self.driver.get(base_url)

    def find_element(self, *locator):
        self.wait_element(locator)
        return self.driver.find_element(*locator)

    def check_element(self, *locator):
        time.sleep(1)
        try:
            return self.driver.find_element(*locator)
        except NoSuchElementException:
            return False

    def open(self, url):
        url = self.base_url + url
        self.driver.get(url)

    def get_title(self):
        return self.driver.title

    def get_url(self):
        return self.driver.current_url

    def hover(self, *locator):
        time.sleep(float(decimal.Decimal(random.randrange(100, 200))/100))
        element = self.find_element(*locator)
        hover = ActionChains(self.driver).move_to_element(element)
        hover.click(on_element=element)
        hover.perform()
        #element.click()


    def switch_iframe(self, element):
        self.driver.switch_to.frame(element)

    def switch_window(self, x):
        self.driver.switch_to.window(self.driver.window_handles[x])

    def wait_element(self, *locator):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(*locator))
        except TimeoutException:
            print("\n * ELEMENT NOT FOUND WITHIN GIVEN TIME! --> %s" %(locator[1]))
            self.driver.quit()