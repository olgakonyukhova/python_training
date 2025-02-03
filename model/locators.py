from selenium.webdriver.common.by import By

class CatalogPageLocators:
    """Локаторы для страницы каталога"""
    CATALOG_BUTTON = (By.XPATH, '//button[@data-qa="header_catalog_nav_open_btn"]')
    ALL_CATEGORIES = (By.XPATH, '//a[@data-qa="all_of_this_category"]')
    PRODUCT_TILES = (By.XPATH, '//a[@data-qa-article]')