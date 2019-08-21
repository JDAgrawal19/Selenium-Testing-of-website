from Manager import Manager
import pytest
from pages.OpenHiwayUrl import OpenHiwayUrl
from pages.Login import Login
from pages.Dashboard import Dashboard
from pages.Timesheet import Timesheet
from pages.StartApp import StartApp
import Utils
import unittest
import constants


class TestTimeSheet(unittest.TestCase):
    @pytest.fixture()
    def setup(self, browser):
        manager = Manager(browser)
        global driver
        driver = manager.get_driver()
        open_hiway = OpenHiwayUrl(driver)
        login_page = Login(driver, constants.primary_user_email_timesheet_tests,
                           constants.primary_user_password_timesheet_tests)
        startapp_page = StartApp(driver)
        dashboard = Dashboard(driver)
        open_hiway.open()
        login_page.enter_email_and_click_next()
        login_page.enter_password_and_click_next()
        startapp_page.go_to_dashboard()
        dashboard.go_to_timesheeet()
        yield
        manager.close_browser()

    @pytest.mark.usefixtures("setup")
    def test_name_on_timesheet(self):
        timesheet = Timesheet(driver)
        user_name = timesheet.get_user_name()
        user_name_from_email = timesheet.get_user_name_from_email()
        assert user_name_from_email in user_name

    @pytest.mark.usefixtures("setup")
    def test_default_date_on_timesheet(self):
        timesheet = Timesheet(driver)
        date_on_timesheet = timesheet.get_date_showing_on_timesheet()
        current_date = Utils.get_current_date_with_format_same_as_timesheet()
        assert current_date in date_on_timesheet
