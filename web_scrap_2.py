import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialzation of Chrome
service = Service()
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=service)

url = "https://contratos.sistema.gov.br/transparencia/arp-item?palavra_chave=equipo&status=todos"
driver.get(url)

#Array - of div
#r = driver.find_elements(By.TAG_NAME, 'div')

#Wait 
print("Waiting for table to load...")
wait = WebDriverWait(driver, 60)  # adjust the timeout to 60 seconds


#Find element
# t = driver.find_elements(By.CLASS_NAME, 'dataTables_wrapper')
# print(t)

# to_text = t[0].text
# print(to_text)

#Find tablerow
# t_row = driver.find_elements(By.TAG_NAME, 'tr')

# t_row_text = t_row[0].text
# print(t_row_text)

#Table responsive
# table_element = driver.find_element(By.CLASS_NAME, 'table-responsive')
# print("Table element:", table_element)]
table_element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'table-responsive')))
print("Table loaded!")
print("Table element:", table_element)

#Base