from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Login(object):
    locator_login_using_google = "LOGIN USING GOOGLE"
    locator_email_text_field = "identifierId"
    locator_email_next_button = "identifierNext"
    locator_password_text_field = "password"
    locator_password_next_button = "passwordNext"

    def __init__(self, driver, username, password):
        self.driver = driver
        self.username = username
        self.password = password

    def enter_email_and_click_next(self):
        self.driver.find_element_by_link_text(self.locator_login_using_google).click()
        self.driver.find_element_by_id(self.locator_email_text_field).send_keys(self.username)
        email_next_button = self.driver.find_element_by_id(self.locator_email_next_button)
        email_next_button.click()
        WebDriverWait(self.driver, 10).until(EC.staleness_of(email_next_button))

    def enter_password_and_click_next(self):
        self.driver.find_element_by_name(self.locator_password_text_field).send_keys(self.password)
        self.driver.find_element_by_id(self.locator_password_next_button).click()


