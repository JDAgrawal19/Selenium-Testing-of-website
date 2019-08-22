import time
import custom_logger as cl
import logging


class Dashboard(object):

    log = cl.custom_logger(logging.DEBUG)

    locator_timesheet_button = "//a[@aria-label='Timesheet']"

    def __init__(self, driver):
        self.driver = driver

    def go_to_timesheeet(self):
        time.sleep(5)   #used exception like presence_of_all_elements_located  but it did not work
        self.driver.find_element_by_xpath(self.locator_timesheet_button).click()
        self.log.info("clicked on timesheet button on dashboard")
