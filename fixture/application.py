class Application:
    def __init__(self):
        from selenium import webdriver
        self.driver = webdriver.Chrome()
        self.driver.set_window_size(1512, 859)

    def destroy(self):
        self.driver.quit()

    def open_site(self, url="https://sokolov.ru/"):
        self.driver.get(url)

    def wait_for_elements(self, locator, timeout=20):
        WebDriverWait(self.driver, timeout).until(
            EC.presence_of_all_elements_located(locator)
        )

    def wait_and_click(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        ).click()