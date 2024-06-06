Projeto Data Engineering - Scraping e Armazenamento de Dados de Livros

Este projeto tem como objetivo extrair informações sobre livros do site https://books.toscrape.com/ utilizando as bibliotecas Selenium e BeautifulSoup em Python, e então armazenar esses dados em um arquivo CSV e em uma tabela PostgreSQL.

Instalação
Clone este repositório:
git clone https://github.com/seu_usuario/seu_repositorio.git

Instale as dependências:
cd seu_repositorio
pip install -r requirements.txt
Certifique-se de ter o PostgreSQL instalado em sua máquina.

Utilização
Execute o script Books_all_pages.py para extrair informações de todos os livros do site e salvar em um arquivo CSV:
python Books_all_pages.py

Em seguida, execute o script csv_to_DB.py para criar uma tabela no PostgreSQL e importar os dados do CSV:
python csv_to_DB.py


Estrutura do Projeto
Books_all_pages.py: Script principal para extrair informações de todos os livros do site.
Books_page_1.py: Script para extrair informações da primeira página do site.
Books_page_1_category.py: Script para extrair informações da primeira página com as categorias .
Data_scrap.py: Módulo contendo funções para realizar o scraping das informações.
books_scraped.csv: Arquivo CSV onde os dados extraídos são salvos.
csv_to_DB.py: Script para criar uma tabela no PostgreSQL e importar os dados do CSV.
install_requirements.py: Script para instalar as dependências do projeto.
requirements.txt: Arquivo contendo as dependências do projeto.


Contato
Para mais informações ou dúvidas, entre em contato pelo email: leonardovidolin93@gmail.com.
