import pytest
from fixture.application import Application
from fixture.CatalogPage import CatalogPage


@pytest.fixture(scope="function")
def app():
    fixture = Application()
    fixture.open_site()
    yield fixture
    fixture.destroy()

@pytest.fixture()
def catalog_page(app):
    return CatalogPage(app.driver)

class TestCatalog:
    def test_catalog(self, catalog_page):
        catalog_page.open_catalog()
        catalog_page.open_all_categories()
        catalog_page.wait_for_product_tiles()

        product_tiles = catalog_page.count_and_log_product_tiles()

        # Проверка количества плиток
        self.assert_tile_count_is_72(product_tiles)

    def assert_tile_count_is_72(self, product_tiles):
        # Проверка, что плиток ровно 72
        assert len(product_tiles) == 72, f"Ожидалось 72 товара, но найдено {len(product_tiles)} плиток"