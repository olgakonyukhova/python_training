import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestCatalog:
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.driver.set_window_size(1512, 859)

    def teardown_method(self, method):
        self.driver.quit()

    def test_catalog(self):
        self.open_site()

        # Локаторы
        catalog_button_locator = (By.XPATH, '//button[@data-qa="header_catalog_nav_open_btn"]')
        all_categories_locator = (By.XPATH, '//a[@data-qa="all_of_this_category"]')
        product_tiles_locator = (By.XPATH, '//a[@data-qa-article]')  # Локатор для всех плиток товаров

        self.open_catalog(catalog_button_locator)

        self.open_all_categories(all_categories_locator)

        self.wait_for_product_tiles(product_tiles_locator)

        product_tiles = self.count_and_log_product_tiles(product_tiles_locator)

        self.assert_tile_count_is_72(product_tiles)

    def assert_tile_count_is_72(self, product_tiles):
        # Проверка, что плиток ровно 72
        assert len(product_tiles) == 72, f"Ожидалось 72 товара, но найдено {len(product_tiles)}"

    def count_and_log_product_tiles(self, product_tiles_locator):
        # Проверяем количество найденных плиток
        product_tiles = self.driver.find_elements(*product_tiles_locator)
        print(f"Найдено плиток: {len(product_tiles)}")  # Выводим количество плиток в консоль
        return product_tiles

    def wait_for_product_tiles(self, product_tiles_locator):
        # Ожидаем, пока появится хотя бы одна плитка товара
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located(product_tiles_locator)
        )

    def open_all_categories(self, all_categories_locator):
        # Ждем и переходим во "Все категории"
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(all_categories_locator)
        ).click()

    def open_catalog(self, catalog_button_locator):
        # Ждем, пока загрузится кнопка "Каталог", и нажимаем
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(catalog_button_locator)
        ).click()

    def open_site(self):
        # Открываем сайт
        self.driver.get("https://sokolov.ru/")