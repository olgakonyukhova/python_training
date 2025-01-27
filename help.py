import pytest
from fixture.application import Application


@pytest.fixture()
def app(request):
    # Инициализация объекта Application
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


class TestCatalog:
    def test_catalog(self, app):
        driver = app.driver

        # Открываем сайт
        driver.get("https://sokolov.ru/")

        # Локаторы
        catalog_button_locator = (By.XPATH, '//button[@data-qa="header_catalog_nav_open_btn"]')
        all_categories_locator = (By.XPATH, '//a[@data-qa="all_of_this_category"]')
        product_tiles_locator = (By.XPATH, '//a[@data-qa-article]')  # Локатор для всех плиток товаров

        # Ждем, пока загрузится кнопка "Каталог", и нажимаем
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(catalog_button_locator)
        ).click()

        # Ждем и переходим во "Все категории"
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(all_categories_locator)
        ).click()

        # Ожидаем, пока появится хотя бы одна плитка товара
        WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located(product_tiles_locator)
        )

        # Проверяем количество найденных плиток
        product_tiles = driver.find_elements(*product_tiles_locator)
        print(f"Найдено плиток: {len(product_tiles)}")  # Выводим количество плиток в консоль

        # Проверка, что плиток ровно 72
        assert len(product_tiles) == 72, f"Ожидалось 72 товара, но найдено {len(product_tiles)}"