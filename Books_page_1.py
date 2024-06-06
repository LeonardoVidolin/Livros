# %% 

import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd
import time
# %% 

# %% Get URL and send GET request
url = "https://books.toscrape.com/"

try:
    response = requests.get(url) # Obter resposta do HTML
    response.raise_for_status() # Levanta uma exceção para códigos de status HTTP de erro
    print("Sucesso")
except requests.exceptions.HTTPError as http_err:
    print(f"Falha HTTP: {http_err}")
except requests.exceptions.ConnectionError as conn_err:
    print(f"Erro de Conexão: {conn_err}")
except requests.exceptions.Timeout as timeout_err:
    print(f"Erro de Timeout: {timeout_err}")
except requests.exceptions.RequestException as req_err:
    print(f"Erro na Requisição: {req_err}")

#response = requests.get(url)
if response.status_code == 200: # Verificar se funcionou
    print("Sucesso")
else:
    print("Falha")


# %% create SOUP object
soup = BeautifulSoup(response.text, "html.parser") 
print(soup)


# %%
# find all 20 books on page 1
books = soup.find_all("article", class_="product_pod")

# Iterate through the books and extract the information for each book
for book in books:
    title = book.h3.a["title"]
    price = book.find("p", class_="price_color").get_text().strip()
    rating = book.p["class"][1]
    stock = book.find("p", class_="instock availability").get_text().strip()
    
    print(f"Title: {title}")
    print(f"Price: {price}")
    print(f"Rating: {rating}")
    print(f"Available: {stock}")