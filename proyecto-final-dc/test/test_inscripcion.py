from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Inicializa el WebDriver
driver = webdriver.Chrome()
driver.get("http://localhost:3000")  # URL de la aplicación
wait = WebDriverWait(driver, 30)  # Incrementar el tiempo de espera

try:
    # Iniciar sesión de forma automática
    print("Iniciando sesión...")

    # Verifica que el campo de usuario esté presente
    username_field = wait.until(EC.presence_of_element_located((By.ID, "username")))  # Asegúrate de que el campo tenga el id 'username'
    if username_field:
        print("Campo de usuario encontrado.")
    username_field.send_keys("admin")  # Ingresar "admin" como usuario

    # Verifica que el botón de login esté disponible y haz clic
    login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Iniciar sesión']")))  # Asegúrate de que el botón sea accesible
    if login_button:
        print("Botón de inicio de sesión encontrado y haciendo clic.")
    login_button.click()

    print("Iniciado sesión correctamente.")

    # Espera y navega a la página 'Gestionar Alumnos'
    print("Navegando a 'Gestionar Alumnos'...")
    wait.until(EC.presence_of_element_located((By.XPATH, "//a[text()='Gestionar Alumnos']"))).click()
    print("Navegación a 'Gestionar Alumnos' exitosa.")

    # Registrar un nuevo alumno
    print("Abriendo formulario de registro de alumno...")
    wait.until(EC.presence_of_element_located((By.XPATH, "//button[text()='Registrar Alumno']"))).click()
    print("Formulario de registro de alumno abierto.")

    # Llenar el formulario de alumno automáticamente
    wait.until(EC.presence_of_element_located((By.ID, "nombre"))).send_keys("Juan Pérez")
    wait.until(EC.presence_of_element_located((By.ID, "apellido"))).send_keys("Gómez")
    wait.until(EC.presence_of_element_located((By.ID, "email"))).send_keys("juan.perez@email.com")
    wait.until(EC.presence_of_element_located((By.ID, "telefono"))).send_keys("123456789")
    wait.until(EC.presence_of_element_located((By.ID, "direccion"))).send_keys("Calle Ficticia 123")

    # Haz clic en el botón para registrar el alumno
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Registrar']"))).click()
    print("Alumno registrado correctamente.")

    # Navegar a 'Gestionar Materias'
    print("Navegando a 'Gestionar Materias'...")
    wait.until(EC.presence_of_element_located((By.XPATH, "//a[text()='Gestionar Materias']"))).click()
    print("Navegación a 'Gestionar Materias' exitosa.")

    # Registrar una nueva materia
    print("Abriendo formulario de registro de materia...")
    wait.until(EC.presence_of_element_located((By.XPATH, "//button[text()='Registrar Materia']"))).click()
    print("Formulario de registro de materia abierto.")

    # Llenar el formulario de materia automáticamente
    wait.until(EC.presence_of_element_located((By.ID, "nombreMateria"))).send_keys("Matemáticas")
    wait.until(EC.presence_of_element_located((By.ID, "codigoMateria"))).send_keys("MAT101")

    # Haz clic en el botón para registrar la materia
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Registrar']"))).click()
    print("Materia registrada correctamente.")

    # Navegar a 'Inscripción'
    print("Navegando a 'Inscripción'...")
    wait.until(EC.presence_of_element_located((By.XPATH, "//a[text()='Inscripción']"))).click()
    print("Navegación a 'Inscripción' exitosa.")

    # Realiza la inscripción de un alumno a una materia
    print("Realizando inscripción...")
    wait.until(EC.presence_of_element_located((By.ID, "alumno"))).send_keys("Juan Pérez")  # Asume que este es el campo para seleccionar alumno
    wait.until(EC.presence_of_element_located((By.ID, "materia"))).send_keys("Matemáticas")  # Asume que este es el campo para seleccionar materia
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Inscribir']"))).click()
    print("Alumno inscrito correctamente en la materia.")

    # Si todo salió bien, indicamos que la prueba fue exitosa
    print("Prueba completada con éxito: Alumno inscrito y materia gestionada.")

except Exception as e:
    print(f"Error durante la prueba: {e}")

finally:
    time.sleep(5)  # Espera unos segundos para ver el resultado antes de cerrar el navegador
    driver.quit()
