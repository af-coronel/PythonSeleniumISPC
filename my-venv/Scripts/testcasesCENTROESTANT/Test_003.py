import unittest
from selenium import webdriver

class TestNavigationBar(unittest.TestCase):
    def setUp(self):
        # Configuración del navegador
        self.driver = webdriver.Chrome()
        self.base_url = "https://centroestant.com.ar/"

    def test_navigation_bar_elements(self):
        # Abrir la página de CENTRO ESTANT
        self.driver.get(self.base_url)

        # Obtener elementos de la barra de navegación
        elementos_nav = self.driver.find_elements("css selector", "#wide-nav .nav-top-link")

        for i in range(len(elementos_nav)):
            # Volver a cargar la página para evitar StaleElementReferenceException
            self.driver.get(self.base_url)
            
            # Obtener nuevamente los elementos de la barra de navegación
            elementos_nav = self.driver.find_elements("css selector", "#wide-nav .nav-top-link")

            # Hacer clic en un elemento de la barra de navegación
            elemento = elementos_nav[i]
            elemento.click()

            # Verificar que se ha redirigido a una nueva página
            self.assertNotEqual(self.base_url, self.driver.current_url)

            # Hacer clic en el icono de la página
            icono_pagina = self.driver.find_element("css selector", "#logo a")
            icono_pagina.click()

            # Verificar que se ha redirigido a la página de inicio
            self.assertEqual(self.base_url, self.driver.current_url)

    def tearDown(self):
        # Cerrar el navegador al finalizar la prueba
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()

