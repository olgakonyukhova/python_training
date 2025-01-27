from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from model.locators import get_catalog_button_locator, get_all_categories_locator, get_product_tiles_locator

class CatalogPage:
    def __init__(self, driver):
        self.driver = driver  # Сохраняем драйвер

    def open_catalog(self):
        catalog_button_locator = get_catalog_button_locator()  # Используем функцию для получения локатора
        self.wait_and_click(catalog_button_locator)

    def open_all_categories(self):
        all_categories_locator = get_all_categories_locator()
        self.wait_and_click(all_categories_locator)

    def wait_for_product_tiles(self):
        product_tiles_locator = get_product_tiles_locator()
        self.wait_for_elements(product_tiles_locator)

    def count_and_log_product_tiles(self):
        product_tiles_locator = get_product_tiles_locator()
        product_tiles = self.driver.find_elements(*product_tiles_locator)
        print(f"Найдено плиток: {len(product_tiles)}")
        return product_tiles

    def wait_for_elements(self, locator, timeout=20):
        WebDriverWait(self.driver, timeout).until(
            EC.presence_of_all_elements_located(locator)
        )

    def wait_and_click(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        ).click()