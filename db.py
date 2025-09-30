
# para conectar ao postgre
import psycopg2 as pg

# pip install dotenv
from dotenv import load_dotenv

import os

#Carreagar as minhas variaveis do .env

load_dotenv()

params = {
    "dbname": os.getenv("DB_NAME"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "host": os.getenv("DB_HOST"),
    "port": os.getenv("DB_PORT"),
}

def conectar():
    try:
        conexao = pg.connect(**params)
        cursor = conexao.cursor()
        print('Deu certo')
        return conexao, cursor
    except Exception as erro:  # Captura qualquer tipo de erro genérico que ocorra no bloco try
        print(f"Erro na conexão {erro}")  # Exibe a mensagem de erro no terminal, mostrando o que deu errado
        return None, None  # Retorna dois valores None, útil quando a função deveria retornar dois objetos (ex: conexão e cursor)
