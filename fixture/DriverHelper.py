from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DriverHelper:
    def __init__(self, driver):
        self.driver = driver

    def wait_element_visible(self, locator, timeout=10):
        """Ожидание появления элемента"""
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    def find_element(self, locator, timeout=10):
        """Ожидание появления элемента и его возврат"""
        return self.wait_element_visible(locator, timeout)

    def wait_for_clickable(self, locator, timeout=10):
        """Ожидание кликабельности элемента"""
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    def click(self, locator, timeout=10):
        """Ожидание кликабельности и клик по элементу"""
        element = self.wait_for_clickable(locator, timeout)
        element.click()