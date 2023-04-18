from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import requests

driver = webdriver.Firefox()
driver.get('https://icp.administracionelectronica.gob.es/icpplus/index.html')

datos = [{"passaporte": "AW985926", "nombre": "Juan david hernandez ayala",
          "nacimiento": 1995, "Pais": "Colombia"},
         {"passaporte": "AW985929q ", "nombre": "Maria Isabel Patiño Villarruel",
         "nacimiento": 1996, "Pais": "Colombia"}

         ]


"""navegar por la pagina"""
try:
    cookies = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "cookie_action_close_header"))
    )
    cookies.click()
except:
    pass
selection = driver.find_element(By.XPATH, "//*[@id='form']/option[16]")
selection.send_keys("Castellón")

driver.implicitly_wait(15)

acept = driver.find_element(By.XPATH, "//*[@id='btnAceptar']").click()

drop = Select(driver.find_element(By.XPATH, "//*[@id='sede']"))
drop.select_by_visible_text("CNP COMISARIA ASILO, RIO SELLA, 5")

droptramit = Select(driver.find_element(
    By.XPATH, "//*[@id='tramiteGrupo[0]']"))
droptramit.select_by_visible_text("POLICIA- SOLICITUD ASILO")

driver.implicitly_wait(30)

acept = driver.find_element(By.XPATH, "//*[@id='btnAceptar']").click()
enter = driver.find_element(By.XPATH, "//*[@id='btnEntrar']").click()

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
        selection = driver.find_element(By.XPATH, "//*[@id='form']/option[16]")
        selection.send_keys("Castellón")

        driver.implicitly_wait(15)

        acept = driver.find_element(By.XPATH, "//*[@id='btnAceptar']").click()

        drop = Select(driver.find_element(By.XPATH, "//*[@id='sede']"))
        drop.select_by_visible_text("CNP COMISARIA ASILO, RIO SELLA, 5")

        droptramit = Select(driver.find_element(
            By.XPATH, "//*[@id='tramiteGrupo[0]']"))
        droptramit.select_by_visible_text("POLICIA- SOLICITUD ASILO")

        driver.implicitly_wait(30)

        acept = driver.find_element(By.XPATH, "//*[@id='btnAceptar']").click()
        enter = driver.find_element(By.XPATH, "//*[@id='btnEntrar']").click()
if repeat == 6:
    driver.quit()
