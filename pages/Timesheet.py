class Timesheet(object):
    locator_username_in_heading = "h2[class='ng-binding']"
    locator_username_in_email = "username-position"
    locator_timesheet_date = "span[class='mobile-timesheet-date ng-binding']"

    def __init__(self, driver):
        self.driver = driver

    def get_user_name(self):
        return self.driver.find_element_by_css_selector(self.locator_username_in_heading).text

    def get_user_name_from_email(self):
        return self.driver.find_element_by_class_name(self.locator_username_in_email).text.split('@')[0].lower().replace('.', ' ')

    def get_date_showing_on_timesheet(self):
        return self.driver.find_element_by_css_selector(self.locator_timesheet_date).text