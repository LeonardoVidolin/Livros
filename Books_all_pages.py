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


# %% Find books on all pages

# Create a list to hold all the books
books_data = []
# loop
for page_num in range(1,51):
    url = f'http://books.toscrape.com/catalogue/page-{page_num}.html'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    books = soup.find_all('h3')

    start_time = time.time()
    books_extracted = 0
    
    for book in books:
        book_url = book.find('a')['href']
        book_response = requests.get('http://books.toscrape.com/catalogue/'+book_url)
        book_soup = BeautifulSoup(book_response.content, "html.parser")

        title = book_soup.find('h1').text
        category = book_soup.find('ul', class_="breadcrumb").find_all('a')[2].text.strip()
        rating = book_soup.find('p', class_='star-rating')['class'][1]
        price = book_soup.find('p', class_='price_color').text.strip()
        availability = book_soup.find('p', class_='availability').text.strip()

        end_time = time.time()
        total_time = (end_time-start_time)/60.0

        books_data.append([title, category, rating, price, availability])
        print(books_data)
        print('*******')
        print(f'total time: {total_time:.2f} minutes')
        print('*******')
        print(f'{page_num * len(books)} Books extrated so far...')
    
# ## Export the data
df = pd.DataFrame(books_data, columns=['Title','Category','Rating','Price','Availability'])
#Display first 5 rows
print(df.head(5))


#save data to csv
df.to_csv(r'D:\Cursos\Livros\books_scraped.csv',index=False, sep=';')
print("data saved")




