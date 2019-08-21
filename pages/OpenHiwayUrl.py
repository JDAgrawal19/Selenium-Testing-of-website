from selenium import webdriver
import pytest
import constants


class OpenHiwayUrl(object):
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get(constants.hiway_url)

