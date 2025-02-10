
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

driver = webdriver.Firefox()
driver.get('https://icp.administracionelectronica.gob.es/icpplus/index.html')

datos = [{"passaporte": "", "nombre": "",
          "nacimiento": 1995, "Pais": ""},
         {"passaporte": " ", "nombre": "",
         "nacimiento": 1996, "Pais": ""}

         ]

"""navegar por la pagina"""
try:
    cookies = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "cookie_action_close_header"))
    )
    cookies.click()
except:
    pass


def province():
    driver.find_element(By.XPATH, "//*[@id='form']/option[16]").click()


province()
driver.implicitly_wait(15)


def aceptbutton():
    driver.find_element(By.XPATH, "//*[@id='btnAceptar']").click()


aceptbutton()


def office():
    # select department of police
    driver.find_element(By.XPATH, "//*[@id='sede']/optgroup/option[2]").click()


office()


def procedure():
    # procedure of department of police
    driver.find_element(
        By.XPATH, "//*[@id='tramiteGrupo[0]']/option[2]").click()  # ->solicitud de asilo


procedure()
driver.implicitly_wait(30)
aceptbutton()


def enter():
    driver.find_element(By.XPATH, "//*[@id='btnEntrar']").click()


enter()
# definir el número de veces que se enviarán los datos
repeat = 6

# enviar los datos x veces sin duplicarlos
datos_enviados = set()
datos_enviados = []
for dato in datos:
    for i in range(repeat):
        # localizar los elementos del formulario
        driver.find_element(By.XPATH, "//*[@id='rdbTipoDocPas']").click()
        pasport = driver.find_element(By.XPATH, "//*[@id='txtIdCitado']")
        nombre = driver.find_element(By.XPATH, "//*[@id='txtDesCitado']")
        year = driver.find_element(By.XPATH, "//*[@id='txtAnnoCitado']")
        pais = driver.find_element(By.XPATH, "//*[@id='txtPaisNac']")

        # ingresar los datos en los campos correspondientes
        pasport.send_keys(dato["passaporte"])
        nombre.send_keys(dato["nombre"])
        year.send_keys(dato["nacimiento"])
        pais.send_keys(dato["Pais"])
        driver.find_element(By.XPATH, "//*[@id='btnEnviar']").click()
        # enviar el formulario
        driver.find_element(By.XPATH, "//*[@id='btnSubmit']").click()
        # se repite 6 veces
        province()
        driver.implicitly_wait(15)
        aceptbutton()
        driver.find_element(
            By.XPATH, "//*[@id='sede']/optgroup/option[2]").click()
        driver.find_element(
            By.XPATH, "//*[@id='tramiteGrupo[0]']/option[2]").click()

        driver.implicitly_wait(30)

        aceptbutton()
        enter()
if repeat == 6:
    driver.quit()
