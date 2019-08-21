from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Login(object):
    def __init__(self, driver, username, password):
        self.driver = driver
        self.username = username
        self.password = password

    def enter_email_and_click_next(self):
        self.driver.find_element_by_link_text("LOGIN USING GOOGLE").click()
        self.driver.find_element_by_id("identifierId").send_keys(self.username)
        email_next_button = self.driver.find_element_by_id("identifierNext")
        email_next_button.click()
        WebDriverWait(self.driver, 10).until(EC.staleness_of(email_next_button))

    def enter_password_and_click_next(self):
        self.driver.find_element_by_name("password").send_keys(self.password)
        self.driver.find_element_by_id("passwordNext").click()


