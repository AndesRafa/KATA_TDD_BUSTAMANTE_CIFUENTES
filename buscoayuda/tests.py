from django.test import TestCase
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.ui import WebDriverWait


# Create your tests here.


class Test(TestCase):
    def setUp(self):
        # self.browser = webdriver.Chrome("C:\\Users\\JUAN CIFUENTES\\chromedriver.exe")
        self.browser = webdriver.Firefox()

        self.browser.implicitly_wait(2)

        self.testComment = {
            'correo': 'correo@dominio.com',
            'comentario': 'Cortez y eficiente!!'
        }

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

        wait = WebDriverWait(driver, 10)
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
        imagen.send_keys(
            'C:\\Users\\JUAN CIFUENTES\\Desktop\\Maestria\\Tercero Maestria\\procesos agiles\\imagenes Kata 2\\carpintero.jpg')

        nombreUsuario = driver.find_element_by_id('id_username')
        nombreUsuario.send_keys('juan645')

        clave = driver.find_element_by_id('id_password')
        clave.send_keys('clave123')

        botonGrabar = driver.find_element_by_id('id_grabar')
        botonGrabar.click()
        driver.implicitly_wait(3)
        span = driver.find_element(By.XPATH, '//span[text()="Juan Daniel Arevalo"]')

        self.assertIn('Juan Daniel Arevalo', span.text)

    def test_verDetalle(self):
        self.browser.get('http://127.0.0.1:8000')
        span = self.browser.find_element(By.XPATH, '//span[text()="Juan Daniel Arevalo"]')
        span.click()

        h2 = self.browser.find_element(By.XPATH, '//h2[text()="Juan Daniel Arevalo"]')

        self.assertIn('Juan Daniel Arevalo', h2.text)

    def test_login(self):
        driver = self.browser
        driver.get('http://localhost:8000')
        link = driver.find_element_by_id('id_login')
        link.click()

        wait = WebDriverWait(driver, 10)

        wait.until(
            EC.element_to_be_clickable((By.ID, 'login_modal')))

        nombreUsuario = driver.find_element_by_id('id_username')
        nombreUsuario.send_keys('juan645')

        clave = driver.find_element_by_id('id_password')
        clave.send_keys('clave123')

        botonIngresar = driver.find_element_by_id('id_grabar')
        botonIngresar.click()

        wait.until(
            EC.element_to_be_clickable((By.ID, 'logout')))

        welcome = driver.find_element_by_id('welcome_user')

        self.assertIn('Juan Daniel', welcome.text)

    def test_edit_registro(self):
        driver = self.browser
        driver.get('http://localhost:8000')
        link = driver.find_element_by_id('id_login')
        link.click()

        wait = WebDriverWait(driver, 10)

        wait.until(
            EC.element_to_be_clickable((By.ID, 'login_modal')))

        nombreUsuario = driver.find_element_by_id('id_username')
        nombreUsuario.send_keys('juan645')

        clave = driver.find_element_by_id('id_password')
        clave.send_keys('clave123')

        botonIngresar = driver.find_element_by_id('id_grabar')
        botonIngresar.click()

        wait.until(
            EC.element_to_be_clickable((By.ID, 'id_update')))

        link = self.browser.find_element_by_id('id_update')
        link.click()

        nombre = self.browser.find_element_by_id('id_nombre')
        nombre.clear()
        nombre.send_keys('Cambio')

        apellidos = self.browser.find_element_by_id('id_apellidos')
        apellidos.clear()
        apellidos.send_keys('Prueba')

        experiencia = self.browser.find_element_by_id('id_aniosExperiencia')
        experiencia.clear()
        experiencia.send_keys('2')

        self.browser.find_element_by_xpath(
            "//select[@id='id_tiposDeServicio']/option[text()='Carpintero']").click()

        telefono = self.browser.find_element_by_id('id_telefono')
        telefono.clear()
        telefono.send_keys('3102698542')

        correo = self.browser.find_element_by_id('id_correo')
        correo.clear()
        correo.send_keys('algo.algo@algo.co')

        imagen = self.browser.find_element_by_id('id_imagen')
        imagen.clear()
        imagen.send_keys(
            'C:\\Users\\JUAN CIFUENTES\\Desktop\\Maestria\\Tercero Maestria\\procesos agiles\\imagenes Kata 2\\carpintero.jpg')

        botonGrabar = self.browser.find_element_by_id('grabar')
        botonGrabar.click()

        wait.until(
            EC.element_to_be_clickable((By.ID, 'logout')))

        welcome = driver.find_element_by_id('welcome_update')
        self.assertIn('Cambio', welcome.text)

    def test_comentario(self):
        testComment = self.testComment
        driver = self.browser
        driver.get('http://localhost:8000')

        span = driver.find_element(
            By.XPATH, '//span[text()="Juan Daniel Arevalo"]')
        span.click()

        wait = WebDriverWait(driver, 10)

        submit = wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'btn-success')))

        correo = driver.find_element_by_id('correo')
        correo.send_keys(testComment.get('correo'))

        comentario = driver.find_element_by_id('comentario')
        comentario.send_keys(testComment.get('comentario'))

        submit.click()

        paragraph = driver.find_element(
            By.XPATH, '//h4[text()="{}"]'.format(testComment.get('correo')))

        paragraph = wait.until(
            EC.element_to_be_clickable((By.XPATH, '//h4[text()="{}"]'.format(testComment.get('correo')))))

        self.assertIn(testComment.get('correo'), paragraph.text)
