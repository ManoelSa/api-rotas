from fastapi import HTTPException
from pydantic import BaseModel
import sqlite3
from dotenv import load_dotenv
import os

load_dotenv()

# Definindo o modelo de dados (Pydantic) para validar as entradas, em caso de dados invalidos ele rejeita
class Item(BaseModel):
    name: str
    description: str
    price: float

#Criado para Personalizar o retorno da resposta
class ItemResponse(BaseModel):
    message: str
    item: Item

# Caminho do banco de dados SQLite
DATABASE_PATH = os.getenv("DATABASE_PATH")

# Função para conectar ao banco e executar SQL
def connect_db():
    try:
        conn = sqlite3.connect(DATABASE_PATH)
        print("Conexao realizada com sucesso")
        return conn
    except sqlite3.Error as e:
        raise HTTPException(status_code=500, detail=f"Erro ao conectar ao banco de dados: {e}")