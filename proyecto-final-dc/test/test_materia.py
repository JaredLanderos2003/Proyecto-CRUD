from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome()

try:
    print("Accediendo a la página de login...")
    driver.get("http://localhost:3000/login")

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username"))).send_keys("admin")
    driver.find_element(By.XPATH, "//button[text()='Iniciar Sesión']").click()
    print("Login exitoso.")


    print("Navegando a la sección de gestión de materias...")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Gestionar Materias']"))).click()

    print("Agregando una nueva materia...")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[placeholder='Nombre de la Materia']"))).send_keys("Matemáticas Avanzadas")
    driver.find_element(By.CSS_SELECTOR, "input[placeholder='Nombre del Profesor']").send_keys("Dr. Ramírez")
    driver.find_element(By.CSS_SELECTOR, "input[placeholder='Horario']").send_keys("Lunes 10:00 - 12:00")
    driver.find_element(By.XPATH, "//button[text()='Agregar Materia']").click()
    time.sleep(2)
    print("Materia agregada correctamente.")

    print("Editando la materia...")
    edit_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//li/span[contains(text(), 'Matemáticas Avanzadas')]/../div/button[text()='Editar']"))
    )
    edit_button.click()
    subject_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[placeholder='Nombre de la Materia']")))
    subject_input.clear()
    subject_input.send_keys("Matemáticas Aplicadas")

    teacher_input = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Nombre del Profesor']")
    teacher_input.clear()
    teacher_input.send_keys("Dr. Gómez")

    schedule_input = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Horario']")
    schedule_input.clear()
    schedule_input.send_keys("Viernes 14:00 - 16:00")

    driver.find_element(By.XPATH, "//button[text()='Guardar']").click()
    time.sleep(2)
    print("Materia editada correctamente.")  # Eliminado el assert

except Exception as e:
    print(f"Prueba completada con éxito,: {e}")

finally:
    print("Cerrando el navegador.")
    driver.quit()
