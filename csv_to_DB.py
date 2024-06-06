import pandas as pd
import psycopg2
from sqlalchemy import create_engine

# Ler o CSV com o delimitador correto
try:
    df = pd.read_csv('D:/Cursos/Livros/books_scraped.csv', sep=';', encoding='utf-8')
except Exception as e:
    print(f"Erro ao ler o CSV: {e}")
    exit()

# Conectar ao banco de dados
try:
    conn = psycopg2.connect(
        host="localhost",  # ou o endereço do seu servidor
        database="exported_books",
        user="postgres",
        password="1123"
    )
    cursor = conn.cursor()
except Exception as e:
    print(f"Erro ao conectar ao banco de dados: {e}")
    exit()

# Crie a string de conexão
try:
    engine = create_engine('postgresql+psycopg2://postgres:1123@localhost/exported_books')
    # Insira o dataframe na tabela
    df.to_sql('exported_books', engine, if_exists='append', index=False)
except Exception as e:
    print(f"Erro ao inserir dados na tabela: {e}")
    cursor.close()
    conn.close()
    exit()

# Iterar sobre as linhas do DataFrame e inserir cada linha na tabela
try:
    for index, row in df.iterrows():
        cursor.execute(
            """
            INSERT INTO "exported_books" ("Title", "Category", "Rating", "Price", "Availability")
            VALUES (%s, %s, %s, %s, %s)
            """,
            (row['Title'], row['Category'], row['Rating'], row['Price'], row['Availability'])
        )
    # Confirme as alterações
    conn.commit()
except Exception as e:
    print(f"Erro ao inserir linhas individualmente: {e}")
    conn.rollback()

# Fechar a conexão
cursor.close()
conn.close()
