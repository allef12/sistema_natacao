from fastapi import FastAPI
from routers import alunos
from routers import pagamentos

app = FastAPI()

@app.get("/")
def inicio():
    return{"mensagem":"API funcionando"}


app.include_router(alunos.router)

app.include_router(pagamentos.router)

