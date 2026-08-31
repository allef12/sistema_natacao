
from fastapi import FastAPI

app = FastAPI() # quando alguém acessa, o app recebe a requisição

@app.get("/") # registra uma rota para requisições GET (buscar informações).
def inicio(): #associa a função a rota
    return{"mensagem":"API funcionando carai"}


