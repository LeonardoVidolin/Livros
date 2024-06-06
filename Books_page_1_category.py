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
    
    
# %% Find books on page 1 with category
books = soup.find_all('h3')

start_time = time.time()
books_extracted = 0

# get all titles
for book in books:
    book_url = book.find('a')['href']
    book_response = requests.get(url+book_url)
    book_soup = BeautifulSoup(book_response.content, "html.parser")
    
    title = book_soup.find('h1').text
    category = book_soup.find('ul', class_="breadcrumb").find_all('a')[2].text.strip()
    rating = book_soup.find('p', class_='star-rating')['class'][1]
    price = book_soup.find('p', class_='price_color').text.strip()
    
    books_extracted += 1
    
    end_time = time.time()
    total_time = (end_time-start_time)/60.0
    
    print(f"Title: {title}")
    print(f"Price: {price}")
    print(f"Rating: {rating}")
    print(f"Available: {stock}")
    print('*********')