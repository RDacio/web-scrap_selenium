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

# Iterate through all 85 pages
for page in range(1, 4):

    table = driver.find_elements(By.TAG_NAME, 'td')
    for i in table:
        print(i.get_attribute("innerHTML"))
    
    print("page",page)
    
    # Click the next button
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)  # Allow time for any scrolling animation
    next_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@class='page-link' and text()='Próximo']")))

    next_button.click()

    time.sleep(10)  # You can adjust this timeout as needed
    
    wait.until(EC.presence_of_all_elements_located((By.XPATH, "//tbody/tr")))
