Feature: Login con POM
  Scenario Outline: Inicio de sesión con credenciales válidas
    Given la aplicación está en la pantalla de login
    When ingreso email "<email>" y password "<password>"
    And presiono login
    Then debería iniciar sesión correctamente

  Examples:
    | email             | password |
    | test@example.com  | 12345    |
