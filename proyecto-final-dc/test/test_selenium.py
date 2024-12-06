from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome()

driver.get("http://localhost:3000") 

wait = WebDriverWait(driver, 10)
username = wait.until(EC.presence_of_element_located((By.ID, "username")))  # Ahora usará el ID

username.send_keys("admin")

login_button = driver.find_element(By.XPATH, "//button[text()='Iniciar Sesión']")  # Usamos XPath para el botón
login_button.click()


time.sleep(3)

driver.save_screenshot("login_screenshot.png")


driver.quit()
