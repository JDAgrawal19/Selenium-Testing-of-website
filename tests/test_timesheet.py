from Manager import Manager
import pytest
from pages.OpenHiwayUrl import OpenHiwayUrl
from pages.Login import Login
from pages.Dashboard import Dashboard
from pages.Timesheet import Timesheet


class TestTimeSheet():
    @pytest.fixture()
    def test_setup(self, browser):
        manager = Manager(browser)
        global driver
        driver = manager.get_driver()
        open_hiway = OpenHiwayUrl(driver)
        login_page = Login(driver)
        dashboard = Dashboard(driver)
        open_hiway.open()
        login_page.enter_email_and_click_next()
        login_page.enter_password_and_click_next()
        dashboard.go_to_dashboard()
        dashboard.go_to_timesheeet()
        yield
        manager.close_browser()

    def test_name_on_timesheet(self, test_setup):
        timesheet = Timesheet(driver)
        user_name = timesheet.get_user_name()
        user_name_from_email = timesheet.get_user_name_from_email()
        assert user_name_from_email in user_name


