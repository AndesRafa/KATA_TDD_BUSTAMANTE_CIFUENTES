from django.test import TestCase
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.ui import WebDriverWait

# Create your tests here.


class Test(TestCase):

    def setUp(self):
        # self.browser = webdriver.Chrome(
        #     "C:\\Users\\JUAN CIFUENTES\\chromedriver.exe")
        self.browser = webdriver.Firefox()

        self.browser.implicitly_wait(2)

    def tearDown(self):
        self.browser.quit()

    def testTitle(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('Busco Ayuda', self.browser.title)

    def test_registro(self):
        driver = self.browser
        driver.get('http://localhost:8000')
        link = driver.find_element_by_id('id_register')
        link.click()

        wait = WebDriverWait(driver, 10);
        element = wait.until(EC.element_to_be_clickable((By.ID, 'register_modal')))

        nombre = driver.find_element_by_id('id_nombre')
        nombre.send_keys('Juan Daniel')

        apellidos = driver.find_element_by_id('id_apellidos')
        apellidos.send_keys('Arevalo')

        experiencia = driver.find_element_by_id('id_aniosExperiencia')
        experiencia.send_keys('5')

        driver.find_element_by_xpath(
            "//select[@id='id_tiposDeServicio']/option[text()='Desarrollador Web']").click()
        telefono = driver.find_element_by_id('id_telefono')
        telefono.send_keys('3173024578')

        correo = driver.find_element_by_id('id_correo')
        correo.send_keys('jd.patino1@uniandes.edu.co')

        imagen = driver.find_element_by_id('id_imagen')
        imagen.send_keys('/home/kubuntu/Pictures/daman.jpeg')

        nombreUsuario = driver.find_element_by_id('id_username')
        nombreUsuario.send_keys('juan645')

        clave = driver.find_element_by_id('id_password')
        clave.send_keys('clave123')

        botonGrabar = driver.find_element_by_id('id_grabar')
        botonGrabar.click()
        driver.implicitly_wait(3)
        span = driver.find_element(By.XPATH, '//span[text()="Juan Daniel Arevalo"]')

        self.assertIn('Juan Daniel Arevalo', span.text)
