from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Configuración del navegador
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# URL de tu aplicación (ajústala si es necesario)
url = 'http://localhost:3000'  # Cambia esta URL si tu app está en otro lugar

# Navegar a la página de bienvenida
driver.get(url)

# Esperar a que la página cargue completamente
time.sleep(2)

# Verificar que el título 'Bienvenido' se muestre correctamente
assert "Bienvenido" in driver.page_source

# Función para hacer clic en un botón y verificar la ruta
def test_navigation(button_text, expected_route):
    button = driver.find_element(By.XPATH, f"//button[contains(text(), '{button_text}')]")
    button.click()
    time.sleep(2)  # Esperar que la navegación ocurra

    # Verificar si la URL ha cambiado a la ruta esperada
    current_url = driver.current_url
    assert expected_route in current_url, f"Esperado que la URL contenga '{expected_route}', pero la URL actual es {current_url}"

# Probar la navegación para cada botón
test_navigation("Gestionar Alumnos", "/students")
test_navigation("Gestionar Materias", "/subjects")
test_navigation("Inscripción", "/enrollments")
test_navigation("Captura de Calificaciones", "/grades")

# Cerrar el navegador
driver.quit()
