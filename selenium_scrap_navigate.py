import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize Chrome
service = Service()
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=service)
wait = WebDriverWait(driver, 45)

url = "https://contratos.sistema.gov.br/transparencia/arp-item?palavra_chave=equipo&status=todos"
driver.get(url)
driver.maximize_window()

# Wait for the table to be populated
wait.until(EC.presence_of_all_elements_located((By.XPATH, "//tbody/tr")))

# Now you can extract the table
table = driver.find_elements(By.TAG_NAME, 'td')

for i in table:
    print(i.get_attribute("innerHTML"))
print("Page source length after waiting:", len(driver.page_source))

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(1)  # Allow time for any scrolling animation

# Find the "Next" button and click it
next_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@class='page-link' and text()='Próximo']")))

next_button.click()

time.sleep(5)  # You can adjust this timeout as needed

# Wait for the table to be populated on the second page
wait.until(EC.presence_of_all_elements_located((By.XPATH, "//tbody/tr")))

# Extract the table on the second page
table_second_page = driver.find_elements(By.TAG_NAME, 'td')

for i in table_second_page:
    print(i.get_attribute("innerHTML"))
print("Page source length on second page:", len(driver.page_source))
next_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@class='page-link' and text()='Próximo']")))

next_button.click()

