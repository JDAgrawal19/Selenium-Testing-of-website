class Timesheet(object):
    locator_username_in_heading = "h2[class='ng-binding']"
    locator_username_in_email = "username-position"
    locator_timesheet_date = "span[class='mobile-timesheet-date ng-binding']"
    locator_next_button_timesheet = "//button[@ng-click='next()']"
    locator_prev_button_timesheet = "//button[@ng-click='prev()']"

    def __init__(self, driver):
        self.driver = driver

    def get_user_name(self):
        return self.driver.find_element_by_css_selector(self.locator_username_in_heading).text

    def get_user_name_from_email(self):
        return self.driver.find_element_by_class_name(self.locator_username_in_email).text.split('@')[0].lower().replace('.', ' ')

    def get_date_showing_on_timesheet(self):
        return self.driver.find_element_by_css_selector(self.locator_timesheet_date).text[17:]

    def check_if_next_button_is_enabled(self):
        return self.driver.find_element_by_xpath(self.locator_next_button_timesheet).is_enabled()

    def click_on_prev_button(self):
        self.driver.find_element_by_xpath(self.locator_prev_button_timesheet).click()

