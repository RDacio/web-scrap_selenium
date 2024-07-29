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

# Navigate to the link
link = "https://contratos.sistema.gov.br/transparencia/arpshow/itens/00137/17686/show"
driver.get(link)

# Wait for the table to be populated
wait.until(EC.presence_of_element_located((By.XPATH, "//tbody[last()]/tr/td[4]")))

# Extract the two values
value1 = driver.find_element(By.XPATH, "//tbody[last()]/tr/td[4]").text
value2 = driver.find_element(By.XPATH, "//tbody[last()]/tr/td[5]").text

print(value1)
print(value2)