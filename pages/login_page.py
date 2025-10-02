from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage(BasePage):
    EMAIL = (AppiumBy.XPATH, '//android.widget.EditText[@resource-id="com.sourcey.materialloginexample:id/input_email"]')
    PASSWORD = (AppiumBy.XPATH, '//android.widget.EditText[@resource-id="com.sourcey.materialloginexample:id/input_password"]')
    LOGIN_BUTTON = (AppiumBy.XPATH, '//android.widget.Button[@resource-id="com.sourcey.materialloginexample:id/btn_login"]')
    HOME_MESSAGE = (AppiumBy.XPATH, '//android.widget.TextView[@text="Hello world!"]')

    def enter_email(self, email):
        self.type(self.EMAIL, email)

    def enter_password(self, password):
        self.type(self.PASSWORD, password)

    def tap_login(self):
        self.click(self.LOGIN_BUTTON)

    def is_logged_in(self, timeout_after_click=10):
        """
        Verifica si se logró el login buscando el mensaje "Hello World!!"
        """
        try:
            WebDriverWait(self.driver, timeout_after_click).until(
                EC.visibility_of_element_located(self.HOME_MESSAGE)
            )
            return True
        except:
            return False
