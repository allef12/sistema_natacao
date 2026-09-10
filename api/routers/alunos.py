from fastapi import APIRouter
from database import conectar
from models import Aluno

router = APIRouter()

@router.get("/alunos")
def listar_alunos():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""SELECT id,nome,telefone,data_nascimento
                      FROM alunos""")

    alunos = cursor.fetchall()

    conn.close()

    resultado = []

    for aluno in alunos:
        dados = {
            "id":aluno.id,
            "nome":aluno.nome,
            "telefone":aluno.telefone,
            "data_nascimento": aluno.data_nascimento
        }
        resultado.append(dados)

    return resultado

@router.get("/alunos/{id}")
def buscar_alunos(id: int):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""SELECT id,nome,telefone,data_nascimento
                       FROM alunos
                       WHERE id = ?""",(id,))
    
    aluno = cursor.fetchone()
    conn.close()

    if aluno is None:
        return {"mensagem":"Não foi encontrado aluno"}

    dados = {
        "id":aluno.id,
        "nome": aluno.nome,
        "telefone": aluno.telefone,
        "data_nascimento": aluno.data_nascimento
        
    }
    return dados
    
#-----------------------------------  
#Rota de cadastro
#-----------------------------------
#aluno → é o dado que a API vai receber.
#Aluno → é o modelo Pydantic que define as regras.
#aluno é declarado dentro da função mesmo
#codigo 201 == CODIGO DE CRIAÇÃO
@router.post("/alunos",status_code=201)
def cadastrar_aluno(aluno:Aluno):
