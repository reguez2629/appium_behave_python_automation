from appium import webdriver
from appium.options.android import UiAutomator2Options
import os
from selenium.common.exceptions import WebDriverException

def before_all(context):
    print("Inicializando driver Appium...")

    app_path = os.path.abspath(os.path.join(os.getcwd(), "app", "LoginExample.apk"))
    if not os.path.exists(app_path):
        raise FileNotFoundError(f"APK no encontrada en: {app_path}. Coloca LoginExample.apk en la carpeta app/")

    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.platform_version = "14"
    options.device_name = "testmovil13"
    options.app = app_path
    options.automation_name = "UiAutomator2"

    appium_url = "http://127.0.0.1:4723"

    try:
        context.driver = webdriver.Remote(appium_url, options=options)
    except WebDriverException:
        # En caso de Appium 1.x
        context.driver = webdriver.Remote(appium_url.rstrip("/") + "/wd/hub", options=options)

    context.driver.implicitly_wait(5)

def after_all(context):
    print("Cerrando driver Appium...")
    if hasattr(context, "driver"):
        try:
            context.driver.quit()
        except Exception as e:
            print("Error cerrando driver:", e)
