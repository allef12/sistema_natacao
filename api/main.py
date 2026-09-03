from fastapi import FastAPI
from database import conectar

app = FastAPI()

@app.get("/")
def inicio():
    return{"mensagem":"API funcionando"}
