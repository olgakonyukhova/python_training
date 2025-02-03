from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from model.locators import CatalogPageLocators  # Импортируем класс локаторов

class CatalogPage:
    def __init__(self, driver):
        self.driver = driver  # Сохраняем драйвер

    def open_catalog(self):
        """Открытие каталога"""
        self.wait_and_click(CatalogPageLocators.CATALOG_BUTTON)

    def open_all_categories(self):
        """Открытие всех категорий"""
        self.wait_and_click(CatalogPageLocators.ALL_CATEGORIES)

    def wait_for_product_tiles(self):
        """Ожидание загрузки карточек товаров"""
        self.wait_for_elements(CatalogPageLocators.PRODUCT_TILES)

    def count_and_log_product_tiles(self):
        """Подсчет и логирование количества карточек товаров"""
        product_tiles = self.driver.find_elements(*CatalogPageLocators.PRODUCT_TILES)
        print(f"Найдено плиток: {len(product_tiles)}")
        return product_tiles

    def wait_for_elements(self, locator, timeout=20):
        """Ожидание появления элементов"""
        WebDriverWait(self.driver, timeout).until(
            EC.presence_of_all_elements_located(locator)
        )

    def wait_and_click(self, locator, timeout=10):
        """Ожидание кликабельности элемента и клик"""
        WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        ).click()