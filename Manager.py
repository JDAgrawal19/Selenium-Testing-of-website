from selenium import webdriver
import constants


class Manager(object):
    def __init__(self, driver_name):
        self.driver_name = driver_name
        self.driver = None
        if self.driver_name.lower() == 'chrome':                              # chrome_options = Options()
            self.driver = webdriver.Chrome(constants.path_chrome_driver)      # chrome_options.add_argument("--headless") , options=chrome_options
        elif self.driver_name.lower() == 'firefox':
            self.driver = webdriver.Firefox(executable_path=constants.path_firefox_driver)

    def get_driver(self):
        return self.driver

    def close_browser(self):
        self.driver.close()
        self.driver.quit()






