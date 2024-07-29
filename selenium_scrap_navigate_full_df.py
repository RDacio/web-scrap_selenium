import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
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

select_element = Select(driver.find_element(By.NAME, "itens_length"))
select_element.select_by_value("100")

# Wait for the table to be populated
wait.until(EC.presence_of_all_elements_located((By.XPATH, "//tbody/tr")))

all_pages = pd.DataFrame()

# Iterate through all 85 pages
for page in range(1, 10):
    table_rows = []
    rows = driver.find_elements(By.TAG_NAME, 'tr')
    for row in rows:
        cols = row.find_elements(By.TAG_NAME, 'td')
        cols = [col.get_attribute("innerHTML") for col in cols]
        table_rows.append([col for col in cols])

    table_rows = table_rows[1:]

    page_df = pd.DataFrame(table_rows, columns=[f"Column {i}" for i in range(len(table_rows[0]))])
    page_df.iloc[:, -1] = page_df.iloc[:, -1].apply(lambda x: x.replace('<a href="/transparencia/arpshow/itens/undefined/undefined/show"></a><a href="', '').replace('" class=""><i class="fas fa-eye"></i></a>', ''))
    print("page",page)
    
    all_pages = pd.concat([all_pages,page_df], ignore_index= True)

    if page < 9:
        # Click the next button
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)  # Allow time for any scrolling animation
        next_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@class='page-link' and text()='Próximo']")))
        next_button.click()
        time.sleep(10)  # You can adjust this timeout as needed
        wait.until(EC.presence_of_all_elements_located((By.XPATH, "//tbody/tr")))


all_pages.columns = ["Número da ata", "Unidade gerenciadora", "Número do item", "Código PDM", "Descrição do item", "Unidade federação", "Fornecedor", "Quantidade registrada", "Saldo para adesões", "Início vigência", "Fim vigência", "Ação"]

all_pages.to_excel('Contratos_Gov_output.xlsx', index= False)

print("DataFrame shape:", all_pages.shape)
print("DataFrame columns:", all_pages.columns)
print("DataFrame head:", all_pages.head())
