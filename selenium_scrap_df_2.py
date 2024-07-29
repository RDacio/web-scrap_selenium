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
table_rows = []
rows = driver.find_elements(By.TAG_NAME, 'tr')
for row in rows:
    cols = row.find_elements(By.TAG_NAME, 'td')
    cols = [col.get_attribute("innerHTML") for col in cols]
    table_rows.append([col for col in cols])

table_rows = table_rows[1:]

df = pd.DataFrame(table_rows, columns=[f"Column {i}" for i in range(len(table_rows[0]))])
df.iloc[:, -1] = df.iloc[:, -1].apply(lambda x: x.replace('<a href="/transparencia/arpshow/itens/undefined/undefined/show"></a><a href="', '').replace(' class=""><i class="fas fa-eye"></i></a>', ''))
#"Número da ata","Unidade gerenciadora","Número do item","Código PDM","Descrição do item","Unidade federação","Fornecedor","Quantidade registrada","Saldo para adesões","Início vigência","Fim vigência","Ação"

print(df)