from selenium import webdriver
import pytest
import constants
import custom_logger as cl
import logging


class OpenHiwayUrl(object):

    log = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get(constants.hiway_url)
        self.log.info("opened hiway url")

