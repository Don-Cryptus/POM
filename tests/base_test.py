import unittest
#from selenium import webdriver
import undetected_chromedriver as uc
#pip install git+https://github.com/ultrafunkamsterdam/undetected-chromedriver.git

class BaseTest(unittest.TestCase):

    def setUp(self):
        print("start")
        self.driver = uc.Chrome()
        #self.driver = webdriver.Chrome()
        self.driver.get("https://google.com")
        self.driver.get("https://soundcloud.com/discover")
        #self.driver.set_window_position(0,0)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPages)
    unittest.TextTestRunner(verbosity=1).run(suite)
