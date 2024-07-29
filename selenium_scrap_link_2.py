from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

def extract_values(link):
    # Initialize Chrome
    service = Service()
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options, service=service)
    wait = WebDriverWait(driver, 45)

    # Navigate to the link
    driver.get(link)

    # Wait for the table to be populated
    wait.until(EC.presence_of_element_located((By.XPATH, "//tbody[last()]/tr/td[4]")))

    # Extract the two values
    value1 = driver.find_element(By.XPATH, "//tbody[last()]/tr/td[4]").text
    value2 = driver.find_element(By.XPATH, "//tbody[last()]/tr/td[5]").text

    # Close the browser
    driver.quit()

    return value1, value2

# Read the Excel file
df = pd.read_excel('C:\\Users\\Rodrigo Dácio\\Documents\\MyCode\\Projects\\web-scrap_selenium\\Contratos_Gov_output_2.xlsx')

# Create a list to store the results
results = []

# Iterate over the links
for index, row in df.head(5).iterrows():
    link = row['Ação']
    value1, value2 = extract_values(link)
    results.append((value1, value2))

print(results)