class StartApp(object):
    locator_username_text = "//div[@class='jumbotron']//h3"
    locator_startapp_button = "btn"

    def __init__(self, driver):
        self.driver = driver

    def get_username_from_startapp_page(self):
        return self.driver.find_element_by_xpath(self.locator_username_text).text

    def go_to_dashboard(self):
        self.driver.find_element_by_class_name(self.locator_startapp_button).click()


