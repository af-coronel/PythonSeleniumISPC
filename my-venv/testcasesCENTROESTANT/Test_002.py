import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestBotonRegistrarse(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://centroestant.com.ar/")

    def tearDown(self):
        self.driver.quit()

    def test_boton_registrarse_valida_formulario(self):
        # Hacer clic en el icono_user para abrir el formulario
        icono_user = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'a.nav-top-link.nav-top-not-logged-in.is-small'))
        )
        icono_user.click()

        # Esperar a que aparezca el botón Registrarse y hacer clic en él
        registrarse_button = WebDriverWait(self.driver, 40).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.woocommerce-Button.woocommerce-form-register__submit'))
        )
        registrarse_button.click()

        # Esperar a que aparezca el mensaje de error
        error_message = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'ul.woocommerce-error'))
        )

        # Verificar el mensaje de error
        self.assertEqual(error_message.text, "Error: Por favor escribe una dirección de correo electrónico válida.")

if __name__ == '__main__':
    unittest.main()

