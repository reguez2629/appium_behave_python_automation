from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find(self, locator):
        return self.driver.find_element(*locator)

    def find_visible(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def click(self, locator, timeout=10):
        el = self.find_visible(locator, timeout)
        el.click()

    def type(self, locator, text, timeout=10):
        el = self.find_visible(locator, timeout)
        el.clear()
        el.send_keys(text)
