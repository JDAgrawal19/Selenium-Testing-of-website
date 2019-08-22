from ddt import ddt, data, unpack, file_data
from Manager import Manager
import pytest
from Utils import get_csv_data
from pages.OpenHiwayUrl import OpenHiwayUrl
from pages.Login import Login
from pages.StartApp import StartApp
import unittest
import constants

@ddt
class TestLogin(unittest.TestCase):
    @pytest.fixture()
    def setup(self, browser):
        manager = Manager(browser)
        global driver
        driver = manager.get_driver()
        open_hiway = OpenHiwayUrl(driver)
        open_hiway.open()
        yield
        manager.close_browser()

    @pytest.mark.usefixtures("setup")
    @data(*get_csv_data(constants.path_login_data_csv))
    @unpack
    def test_valid_login(self, username, password):
        login_page = Login(driver, username, password)
        startapp_page = StartApp(driver)
        login_page.enter_email_and_click_next()
        login_page.enter_password_and_click_next()
        assert username in startapp_page.get_username_from_startapp_page()


