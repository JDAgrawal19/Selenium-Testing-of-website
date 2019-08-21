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
from Utils import get_csv_data
from ddt import ddt, data, unpack


@ddt
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

    @pytest.mark.usefixtures("setup")
    def test_next_button_disability_for_current_date(self):
        timesheet = Timesheet(driver)
        date_on_timesheet = timesheet.get_date_showing_on_timesheet()
        current_date = Utils.get_current_date_with_format_same_as_timesheet()
        next_btn_enabled = timesheet.check_if_next_button_is_enabled()
        if current_date in date_on_timesheet:
            assert next_btn_enabled is False

    @pytest.mark.usefixtures("setup")
    def test_click_prev_button_check_prev_date_timesheet(self):
        timesheet = Timesheet(driver)
        for i in range(1, 5):
            timesheet.click_on_prev_button()
            prev_date = Utils.get_date_before_n_number_of_days_with_format_of_timesheet(i)
            date_on_timesheet = timesheet.get_date_showing_on_timesheet()
            assert prev_date in date_on_timesheet

    @pytest.mark.usefixtures("setup")
    @data(*get_csv_data(constants.path_test_added_entry_in_timesheet_csv))
    @unpack
    def test_task_added_in_timesheet_table(self, text, entry_type, hours, minutes, desc):
        timesheet = Timesheet(driver)
        timesheet.delete_all_entries_from_timesheet()
        timesheet.add_entry_to_timesheet_table(text, entry_type, hours, minutes, desc)
        assert timesheet.get_serial_no_of_first_entry() == '1.'

    @pytest.mark.usefixtures("setup")
    @data(*get_csv_data(constants.path_test_added_entry_in_timesheet_csv))
    @unpack
    def test_working_hours_on_adding_new_entry_added(self, text, entry_type, hours, minutes, desc):
        timesheet = Timesheet(driver)
        timesheet.delete_all_entries_from_timesheet()
        timesheet.add_entry_to_timesheet_table(text, entry_type, hours, minutes, desc)
        working_hours = timesheet.get_total_working_hours()
        assert hours in working_hours














    # @pytest.mark.usefixtures("setup")
    # def test_deletion_of_task(self):
    #     timesheet = Timesheet(driver)
    #     timesheet.delete_entry_from_timesheet()










