from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium .webdriver.common.keys import Keys
import time

class Timesheet(object):
    locator_username_in_heading = "h2[class='ng-binding']"
    locator_username_in_email = "username-position"
    locator_timesheet_date = "span[class='mobile-timesheet-date ng-binding']"
    locator_next_button_timesheet = "//button[@ng-click='next()']"
    locator_prev_button_timesheet = "//button[@ng-click='prev()']"
    locator_popup = "div[class = 'md-toast-content']"
    locator_popup_exceed_24 = "//div[@class = 'md-toast-content']/span"
    locator_delete_button = "//form//md-icon-button/md-icon/i"
    locator_entries = "//form/div[@ng-repeat='entry in timeEntry track by $index']"
    locator_add_project_code = '//input[@type="search"]'
    locator_add_entry_type = '//md-select[@ng-model="newEntry.type"]'
    locator_add_hour = "newEntry.hrs"
    locator_add_minute = "newEntry.min"
    locator_add_description = "newEntry.description"
    locator_add_entry_button = "//form//button[@type='submit']"
    locator_serial_no_of_first_entry_timesheet = '//form/div[1]/div[1]/div[1]/div[1]'
    locator_color_bar = '.md-bar.md-bar2'
    locator_empty_timesheet_message = "//md-content//div[@ng-if='timeEntry.length == 0']/i"

    def __init__(self, driver):
        self.driver = driver

    def get_user_name(self):
        return self.driver.find_element_by_css_selector(self.locator_username_in_heading).text

    def get_user_name_from_email(self):
        return self.driver.find_element_by_class_name(self.locator_username_in_email).text.split('@')[0].lower().replace('.', ' ')

    def get_date_showing_on_timesheet(self):
        return self.driver.find_element_by_css_selector(self.locator_timesheet_date).text[17:]

    def get_total_working_hours(self):
        return self.driver.find_element_by_css_selector(self.locator_timesheet_date).text[:5]

    def check_if_next_button_is_enabled(self):
        return self.driver.find_element_by_xpath(self.locator_next_button_timesheet).is_enabled()

    def click_on_prev_button(self):
        self.driver.find_element_by_xpath(self.locator_prev_button_timesheet).click()

    def fill_project_code_in_an_entry(self, text='BUZZAUTO'):
        project_code = self.driver.find_element_by_xpath(self.locator_add_project_code)
        project_code.clear()
        project_code.send_keys(text)

    def fill_type_in_an_entry(self, entry_type='Dev'):
        type_of_entry = self.driver.find_element_by_xpath(self.locator_add_entry_type)
        type_of_entry.send_keys(entry_type)

    def fill_hours_in_an_entry(self, hour ='05'):
        hour_field = self.driver.find_element_by_name(self.locator_add_hour)
        hour_field.clear()
        hour_field.send_keys(hour)

    def fill_minute_in_an_entry(self, minute = '20'):
        minute_field = self.driver.find_element_by_name(self.locator_add_minute)
        minute_field.clear()
        minute_field.send_keys(minute)

    def fill_description_in_an_entry(self, desc='Add a new Entry'):
        desc_field = self.driver.find_element_by_name(self.locator_add_description)
        desc_field.clear()
        desc_field.send_keys(desc)

    def click_add_button_in_entry(self):
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.locator_add_entry_button))
        )
        self.driver.find_element_by_xpath(self.locator_add_entry_button).click()

    def check_if_add_is_clickable(self):
        return self.driver.find_element_by_xpath(self.locator_add_entry_button).is_enabled()

    def add_entry_to_timesheet_table(self, text='ARU-CCUI-DEL', entry_type="Debug", hours='4', minutes='20', desc='Add entry'):
        self.fill_project_code_in_an_entry(text)
        self.fill_type_in_an_entry(entry_type)
        self.fill_hours_in_an_entry(hours)
        self.fill_minute_in_an_entry(minutes)
        self.fill_description_in_an_entry(desc)
        self.click_add_button_in_entry()
        time.sleep(1)

    def get_bar_color_rgb_value(self):
        return str(self.driver.find_element_by_css_selector(self.locator_color_bar)
                   .value_of_css_property('background-color'))

    def delete_all_entries_from_timesheet(self):
        while True:
            try:
                self.driver.find_element_by_xpath(self.locator_delete_button).click()
                self.wait_till_popup_disappear()
            except NoSuchElementException:
                return

    def wait_till_popup_disappear(self):
        popup = self.driver.find_element_by_css_selector(self.locator_popup)
        WebDriverWait(self.driver, 10).until(
            EC.staleness_of(popup))

    def get_message_when_timesheet_is_empty(self):
        return self.driver.find_element_by_xpath(self.locator_empty_timesheet_message).text

    def get_serial_no_of_first_entry(self):
        return str(self.driver.find_element_by_xpath(self.locator_serial_no_of_first_entry_timesheet).text)

    def get_message_from_popup(self):
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.CSS_SELECTOR, self.locator_popup))) #TimeOutException
        WebDriverWait(self.driver, 10).until(
             EC.visibility_of_element_located((By.XPATH, self.locator_popup_exceed_24))) #TimeOutException
        return str(self.driver.find_element_by_xpath(self.locator_popup_exceed_24).text)
