from fastapi import FastAPI
from database import conectar

app = FastAPI()

@app.get("/")
def inicio():
    return{"mensagem":"API funcionando"}


@app.get("/alunos")
def alunos():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""SELECT id,nome,telefone,data_nascimento FROM alunos""")

    alunos = cursor.fetchall()

    conn.close()
