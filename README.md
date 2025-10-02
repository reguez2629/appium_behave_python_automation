1️⃣ Descripción

Este proyecto automatiza el inicio de sesión de la aplicación LoginExample usando Appium con Python, Behave y el patrón Page Object Model (POM).

Permite verificar que:

La app se abre correctamente.

El login con email y password funciona.

Se muestra el mensaje de bienvenida "Hello World!!" después de iniciar sesión.

2️⃣ Estructura del proyecto
appium_behave_login
app/LoginExample.apk       # APK de la aplicación
features/environment.py    # Hooks para setup y teardown de Appium
login.feature              # Feature de inicio de sesión
steps/login_steps.py       # Steps de Behave para login
pages/
__init__.py
base_page.py               # Métodos genéricos de interacción
login_page.py              # Page Object de pantalla de login
requirements.txt           # Dependencias de Python

3️⃣ Requisitos previos

Python 3.10+

Appium Server 2.x instalado y corriendo.

Emulador Android o dispositivo físico con depuración USB activada.

Instalar dependencias:

pip install -r requirements.txt


Contenido sugerido de requirements.txt:

behave==1.2.6
appium-python-client==3.1.1
selenium==4.12.0

4️⃣ Configuración de Appium (environment.py)

from appium import webdriver
from appium.options.android import UiAutomator2Options
import os

def before_all(context):
    app_path = os.path.abspath(os.path.join(os.getcwd(), "app", "LoginExample.apk"))
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.platform_version = "11"
    options.device_name = "emulator-5554"
    options.app = app_path
    options.automation_name = "UiAutomator2"

    context.driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
    context.driver.implicitly_wait(5)

def after_all(context):
    if hasattr(context, "driver"):
        context.driver.quit()


Ajusta platform_version y device_name según tu emulador o dispositivo.

5️⃣ Ejecutar el test de login

Desde la carpeta raíz del proyecto:

behave features/login.feature


Esto ejecutará el escenario de inicio de sesión y verificará que aparece "Hello World!!".

6️⃣ Contenido de login.feature
Feature: Verificar inicio de sesión
  Scenario: Inicio de sesión exitoso
    Given la aplicación está en la pantalla de login
    When ingreso email "user@example.com" y password "12345"
    And presiono login
    Then debería ver el mensaje de bienvenida "Hello World!!"
