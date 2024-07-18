import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize Chrome
service = Service()
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=service)
wait = WebDriverWait(driver, 45)

url = "https://contratos.sistema.gov.br/transparencia/arp-item?palavra_chave=equipo&status=todos"
driver.get(url)
print("Page source length before waiting:", len(driver.page_source))
driver.implicitly_wait(30)
# Wait for the element to be visible; #'a' almost
t = driver.find_elements(By.TAG_NAME, 'tr')

print(t)


print("Page source length after waiting:", len(driver.page_source))
# Once the element is found, you 
# can proceed with extracting the table data

#A lot of garb