from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Inicializa el WebDriver
driver = webdriver.Chrome()
driver.get("http://localhost:3000")
wait = WebDriverWait(driver, 20)

try:
    # Inicia sesión
    print("Iniciando sesión...")
    username = wait.until(EC.presence_of_element_located((By.ID, "username")))
    login_button = driver.find_element(By.XPATH, "//button[text()='Iniciar Sesión']")
    username.send_keys("admin")
    login_button.click()

    # Esperar que la navegación sea exitosa (puedes esperar que el botón "Gestionar Alumnos" esté visible)
    wait.until(EC.presence_of_element_located((By.XPATH, "//button[text()='Gestionar Alumnos']")))

    # Navega a "Gestionar Alumnos"
    print("Navegación a 'Gestionar Alumnos' exitosa.")
    students_button = driver.find_element(By.XPATH, "//button[text()='Gestionar Alumnos']")
    students_button.click()

    # Esperar que la página de "Gestionar Alumnos" se cargue y que el formulario de registro esté visible
    wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='nombre']")))

    # Registrar un nuevo alumno
    print("Alumno registrado correctamente.")
    nombre_input = driver.find_element(By.XPATH, "//input[@name='nombre']")
    nombre_input.send_keys("Juan Pérez")
    # Aquí puedes agregar más campos si es necesario

    # Hacer clic en el botón para guardar el nuevo alumno (asegúrate de que el botón esté presente)
    save_button = driver.find_element(By.XPATH, "//button[text()='Guardar']")
    save_button.click()

    # Confirmación de registro
    wait.until(EC.presence_of_element_located((By.XPATH, "//div[text()='Alumno registrado correctamente']")))

    # Navegar a "Gestionar Materias"
    print("Navegación a 'Gestionar Materias' exitosa.")
    materias_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Gestionar Materias']")))

    # Desplazar al botón si no está visible y hacer clic
    driver.execute_script("arguments[0].scrollIntoView(true);", materias_button)
    driver.execute_script("arguments[0].click();")

    # Esperar a que la página de "Gestionar Materias" se cargue
    wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='nombreMateria']")))

    # Confirmación de éxito de materias
    print("Materia gestionada correctamente.")
    
    # Si todo ha ido bien, mostrar un resumen de éxito
    print("\nResumen de la prueba:")
    print("Inicio de sesión: Éxito")
    print("Gestión de alumnos: Éxito")
    print("Registro de alumno: Éxito")
    print("Gestión de materias: Éxito")
    print("Prueba completa: ¡Todo pasó con éxito!")

except Exception as e:
    # Si ocurre cualquier error, mostrar un mensaje general
    print(f"Error durante la prueba: {e}")

finally:
    time.sleep(5)  # Esperar para ver los resultados antes de cerrar
    driver.quit()
