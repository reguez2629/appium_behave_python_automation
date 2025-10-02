from behave import given, when, then
from pages.login_page import LoginPage

@given("la aplicación está en la pantalla de login")
def step_impl(context):
    context.login_page = LoginPage(context.driver)

@when('ingreso email "{email}" y password "{password}"')
def step_impl(context, email, password):
    context.login_page.enter_email(email)
    context.login_page.enter_password(password)

@when("presiono login")
def step_impl(context):
    context.login_page.tap_login()

@then("debería iniciar sesión correctamente")
def step_impl(context):
    assert context.login_page.is_logged_in(), "No se detectó el mensaje 'Hello World!!'. Login fallido."
