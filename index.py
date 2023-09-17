from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Edge()
wait = WebDriverWait(driver, 10)

driver.get("https://sede.administracionespublicas.gob.es/pagina/index/directorio/icpplus")

# Esperar a que el botón de acceso esté disponible
acceder_procedimiento = wait.until(EC.presence_of_element_located((By.ID, "submit")))
acceder_procedimiento.click()

# Esperar a que el formulario de provincias esté disponible
provincias = wait.until(EC.presence_of_element_located((By.ID, "form")))
provincia_a_seleccionar = provincias.find_elements(By.TAG_NAME, "option")[33]
provincia_a_seleccionar.click()

# Esperar a que el botón Aceptar esté disponible y hacer clic
btnAceptar = wait.until(EC.presence_of_element_located((By.ID, "btnAceptar")))
btnAceptar.click()

# Hacer clic en la opción de sedes
sedes = wait.until(EC.presence_of_element_located((By.ID, "sede")))
action = ActionChains(driver)
action.move_to_element(nie).click().perform()

# Seleccionar la primera sede
sedes_a_seleccionar = driver.find_elements(By.TAG_NAME, "option")[0]
sedes_a_seleccionar.click()

# Hacer clic en el tipo de trámite "NIE"
nie = wait.until(EC.presence_of_element_located((By.ID, "tramiteGrupo[0]")))
action = ActionChains(driver)
action.move_to_element(nie).click().perform()

# Seleccionar el tercer tipo de trámite para NIE
nie_a_seleccionar = driver.find_elements(By.TAG_NAME, "option")[1]
nie_a_seleccionar.click()

# Hacer clic en el botón Aceptar después de seleccionar el trámite
btnAceptar2 = wait.until(EC.presence_of_element_located((By.ID, "btnAceptar")))
btnAceptar2.click()

# Hacer clic en el botón Entrar para continuar
btnEntrar = wait.until(EC.presence_of_element_located((By.ID, "btnEntrar")))
btnEntrar.click()

# Recuerda cerrar el navegador al finalizar
driver.quit()

nie_a_seleccionar = nie[3]
nie_a_seleccionar.click()
wait = WebDriverWait(driver, 10)

btnAceptar2 = driver.find_element("id","btnAceptar")
btnAceptar2.click()
wait = WebDriverWait(driver, 10)

btnEntrar = driver.find_element("id","btnEntrar")
btnEntrar.click()
wait = WebDriverWait(driver, 10)
