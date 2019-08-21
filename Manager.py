from selenium import webdriver
import constants


class Manager(object):
    def __init__(self, driver_name):
        self.driver_name = driver_name
        self.driver = None
        if self.driver_name.lower() == 'chrome':
            self.driver = webdriver.Chrome(constants.path_chrome_driver)
        elif self.driver_name.lower() == 'firefox':
            self.driver = webdriver.Firefox(executable_path=constants.path_firefox_driver)

    def get_driver(self):
        return self.driver

    def close_browser(self):
        self.driver.close()
        self.driver.quit()






