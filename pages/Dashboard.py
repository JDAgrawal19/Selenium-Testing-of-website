import time


class Dashboard(object):
    def __init__(self, driver):
        self.driver = driver

    def go_to_dashboard(self):
        self.driver.find_element_by_class_name("btn").click()

    def go_to_timesheeet(self):
        time.sleep(5)
        self.driver.find_element_by_xpath("//a[@aria-label='Timesheet']").click()
