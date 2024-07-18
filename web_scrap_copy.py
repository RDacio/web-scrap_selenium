import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the Chrome driver
driver = webdriver.Chrome()

# Navigate to the website
driver.get("https://contratos.sistema.gov.br/transparencia/arp-item?palavra_chave=equipo&status=todos")

# Not waiting 
table_element = WebDriverWait(driver, 30).until(
    EC.presence_of_all_elements_located((By.TAG_NAME, 'tr'))
)
print(table_element)

print("Table found!")

#Almost