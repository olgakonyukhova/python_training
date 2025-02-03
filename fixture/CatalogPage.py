from model.locators import CatalogPageLocators
from .driver_helper import DriverHelper

class CatalogPage:
    def __init__(self, driver):
        self.driver = driver
        self.helper = DriverHelper(driver)  # Создаем объект DriverHelper

    def open_catalog(self):
        """Открытие каталога"""
        self.helper.click(CatalogPageLocators.CATALOG_BUTTON)

    def open_all_categories(self):
        """Открытие всех категорий"""
        self.helper.click(CatalogPageLocators.ALL_CATEGORIES)

    def wait_for_product_tiles(self):
        """Ожидание загрузки карточек товаров"""
        self.helper.wait_element_visible(CatalogPageLocators.PRODUCT_TILES)

    def count_and_log_product_tiles(self):
        """Подсчет и логирование количества карточек товаров"""
        product_tiles = self.driver.find_elements(*CatalogPageLocators.PRODUCT_TILES)
        print(f"Найдено плиток: {len(product_tiles)}")
        return product_tiles