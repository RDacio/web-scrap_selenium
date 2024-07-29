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

# Create a Pandas DataFrame with 12 columns
df = pd.DataFrame(columns=['Column1', 'Column2', 'Column3', 'Column4', 
                           'Column5', 'Column6', 'Column7', 'Column8', 
                           'Column9', 'Column10', 'Column11', 'Column12'])

# Extract the table data
table_rows = driver.find_elements(By.TAG_NAME, 'tr')
for row in table_rows:
    cols = row.find_elements(By.TAG_NAME, 'td')
    row_data = [i.get_attribute("innerHTML") for i in cols]
    print(row_data)

