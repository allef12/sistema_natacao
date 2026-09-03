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

    resultado = []

    for aluno in alunos:
        dados = {
            "id":aluno.id,
            "nome":aluno.nome,
            "telefone":aluno.telefone,
            "data_nascimento":aluno.data_nascimento
        }
        resultado.append(dados)

    return resultado