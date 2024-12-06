from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Configuración del navegador
driver = webdriver.Chrome()

try:
    # 1. Acceder al login
    print("Accediendo al login...")
    driver.get("http://localhost:3000/login")

    # Esperar que el campo de username esté presente y luego enviar 'admin'
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username"))).send_keys("admin")
    
    # Hacer clic en el botón de iniciar sesión
    driver.find_element(By.XPATH, "//button[text()='Iniciar Sesión']").click()
    print("Login exitoso.")

    # 2. Navegar a la sección de captura de calificaciones
    print("Navegando a la sección de captura de calificaciones...")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Captura de Calificaciones']"))).click()

    # 3. Seleccionar inscripción
    print("Seleccionando inscripción...")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//select[@value='']")))

    # Seleccionar inscripción: 'Jared Noe Landeros → Desarrollo Colaborativo'
    driver.find_element(By.XPATH, "//option[text()='Jared Noe Landeros → Desarrollo Colaborativo']").click()

    # 4. Ingresar calificación
    print("Ingresando la calificación...")
    input_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[placeholder='Calificación']"))
    )
    input_field.clear()  # Limpiar el campo en caso de que haya algún valor previo
    input_field.send_keys("85")

    # 5. Hacer clic en el botón de 'Capturar'
    driver.find_element(By.XPATH, "//button[text()='Capturar']").click()

    # 6. Verificar si la calificación fue capturada correctamente
    print("Verificando si la calificación fue capturada...")
    time.sleep(2)  # Esperar que la lista de calificaciones se actualice

    # Verificar que la calificación aparece en la lista
    grades_list = driver.find_elements(By.XPATH, "//li[contains(text(), 'Jared Noe Landeros → Desarrollo Colaborativo: 85')]")
    assert len(grades_list) > 0, "Error: La calificación no fue capturada correctamente."

    print("Calificación capturada correctamente.")



finally:
    print("Cerrando el navegador.")
    driver.quit()
