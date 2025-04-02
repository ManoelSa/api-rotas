from fastapi import FastAPI
from rotas import create_produto, get_produto, update_produto, delete_produto

app = FastAPI()

app.include_router(create_produto.router)
app.include_router(get_produto.router)
app.include_router(update_produto.router)
app.include_router(delete_produto.router)

@app.get("/")
def read_root():
    return {"message": "Bem vindo a base Cadastral API MM"}