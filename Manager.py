from selenium import webdriver


class Manager(object):
    def __init__(self, driver_name):
        self.driver_name = driver_name
        self.driver = None
        if self.driver_name.lower() == 'chrome':
            self.driver = webdriver.Chrome("/home/jitesh_dhoot/Selenium-track/mydriver/chromedriver")
        elif self.driver_name.lower() == 'firefox':
            self.driver = webdriver.Firefox(executable_path="/home/jitesh_dhoot/Selenium-track/mydriver/geckodriver")

    def get_driver(self):
        return self.driver

    def close_browser(self):
        self.driver.close()
        self.driver.quit()






