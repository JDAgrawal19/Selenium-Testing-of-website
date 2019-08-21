from ddt import ddt, data, unpack, file_data
from Manager import Manager
import pytest
from Utils import get_csv_data
from pages.OpenHiwayUrl import OpenHiwayUrl
from pages.Login import Login


@ddt
class TestLogin(object):
    @pytest.fixture()
    def test_setup(self, browser):
        manager = Manager(browser)
        global driver
        driver = manager.get_driver()
        open_hiway = OpenHiwayUrl(driver)
        open_hiway.open()
        yield
        manager.close_browser()

    @pytest.mark.usefixtures("test_setup")
    @data(get_csv_data("/home/jitesh_dhoot/Selenium-track/tests/data.csv"))
    @unpack
    def test_valid_login(self, username, password):
        login_page = Login(driver, username, password)
        login_page.enter_email_and_click_next()
        login_page.enter_password_and_click_next()
