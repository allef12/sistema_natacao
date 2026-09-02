
from fastapi import FastAPI
from database import conectar

app = FastAPI() # quando alguém acessa, o app recebe a requisição

@app.get("/") # registra uma rota para requisições GET (buscar informações).
def inicio(): #associa a função a rota
    return{"mensagem":"API funcionando"}

@app.get("/alunos")
def listar_alunos():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""SELECT id,nome,telefone,data_nascimento
                      FROM alunos""")

    alunos = cursor.fetchall()

    conn.close


