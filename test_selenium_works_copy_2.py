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
# Wait for the table to be populated
wait.until(EC.presence_of_all_elements_located((By.XPATH, "//tbody/tr")))
print('wait')
# Now you can extract the table
table = driver.find_elements(By.TAG_NAME, 'td')

print('done')

for i in table:
    print(i.get_attribute("innerHTML"))
print("Page source length after waiting:", len(driver.page_source))
# Once the element is found, you 
# can proceed with extracting the table data

#A lot of garb