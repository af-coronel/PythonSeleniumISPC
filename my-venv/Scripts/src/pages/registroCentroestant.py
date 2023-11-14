from selenium.webdriver.common.by import By

class RegistroPage:
    def __init__(self, driver):
        self.driver = driver
        self.email_input = (By.ID, "reg_email")
        self.password_input = (By.ID, "reg_password")
        self.register_button = (By.NAME, "register")

    def navigate_to_registration_page(self):
        #Navega a la página de Centroestant
        self.driver.get("https://centroestant.com.ar/")
          
    def registrar_usuario(self, email, password):
        # Asegúra que el formulario esté abierto haciendo clic en el botón de registro
        self.driver.find_element(By.ID, "tu_id_del_boton_registro").click()

        # Completa el formulario de registro
        self.driver.find_element(*self.email_input).send_keys(email)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.register_button).click()
        
