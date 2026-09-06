from fastapi import APIRouter
from database import conectar

router = APIRouter()

@router.get("/alunos")
def listar_alunos():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""SELECT id,nome,telefone,data_nascimento
                      FROM alunos""")

    alunos = cursor.fetchall()

    conn.close()

