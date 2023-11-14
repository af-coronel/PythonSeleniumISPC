
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

class TestBotonLogin(unittest.TestCase):

    def setUp(self):
        # Configuración previa a la ejecución del caso de prueba
        self.driver = webdriver.Chrome()
        self.driver.get("https://centroestant.com.ar/")

    def test_clic_en_boton_login_redirecciona_a_pagina_registro(self):
        # Espera a que el botón de login sea interactuable
        try:
            boton_login = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "nav-top-link"))
            )
        except TimeoutException:
            self.fail("El botón de login no fue interactuable después de 10 segundos.")

        # Encuentra el botón de login por la clase y hacer clic en él
        boton_login.click()

        # Verifica que la página se redirige a la URL esperada
        url_esperada = "https://centroestant.com.ar/"
        try:
            WebDriverWait(self.driver, 10).until(
                EC.url_to_be(url_esperada)
            )
        except TimeoutException:
            self.fail(f"La página no se redirigió a la URL esperada: {url_esperada}")

    def tearDown(self):
        # Acciones después de la ejecución del caso de prueba
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()

