from selenium.webdriver.common.by import By

def get_catalog_button_locator():
    return (By.XPATH, '//button[@data-qa="header_catalog_nav_open_btn"]')

def get_all_categories_locator():
    return (By.XPATH, '//a[@data-qa="all_of_this_category"]')

def get_product_tiles_locator():
    return (By.XPATH, '//a[@data-qa-article]')