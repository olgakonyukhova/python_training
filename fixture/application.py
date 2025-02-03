from fixture.driver_helper import DriverHelper


class Application:
    def __init__(self):
        from selenium import webdriver
        self.driver = webdriver.Chrome()
        self.driver.set_window_size(1512, 859)
        self.driver_helper = DriverHelper(self.driver)

    def destroy(self):
        self.driver.quit()

    def open_site(self, url="https://sokolov.ru/"):
        self.driver.get(url)

    def wait_for_elements(self, locator, timeout=20):
        self.driver_helper.wait_element_visible(locator, timeout)

    def wait_and_click(self, locator, timeout=10):
        self.driver_helper.wait_for_clickable(locator, timeout)
        self.driver_helper.click(locator)