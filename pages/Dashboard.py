import time


class Dashboard(object):
    locator_timesheet_button = "//a[@aria-label='Timesheet']"

    def __init__(self, driver):
        self.driver = driver

    def go_to_timesheeet(self):
        time.sleep(5)
        self.driver.find_element_by_xpath(self.locator_timesheet_button).click()
