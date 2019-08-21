class Timesheet(object):
    def __init__(self, driver):
        self.driver = driver

    def get_user_name(self):
        return self.driver.find_element_by_css_selector("h2[class='ng-binding']").text

    def get_user_name_from_email(self):
        return self.driver.find_element_by_class_name("username-position").text.split('@')[0].lower().replace('.', ' ')