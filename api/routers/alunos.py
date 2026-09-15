from fastapi import APIRouter
from database import conectar
from models import Aluno

router = APIRouter()
#---------------------------
#ROTA BUSCA TODOS OS ALUNOS
#---------------------------
@router.get("/alunos", tags=["Alunos"])
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
#---------------------------
#ROTA BUSCA  OS ALUNOS ESPECÍFICOS
#---------------------------
@router.get("/alunos/{id}", tags=["Alunos"])
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
@router.post("/alunos",status_code=201, tags=["Alunos"])
def cadastrar_aluno(aluno:Aluno):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""INSERT INTO alunos (nome,telefone,data_nascimento)
                      OUTPUT INSERTED.id VALUES(?,?,?)""",
                      (aluno.nome,aluno.telefone,aluno.data_nascimento.strftime("%Y/%m/%d")
                       ))
    novo_id = cursor.fetchone()[0]
    conn.commit()
    conn.close()

    return {"mensagem":"Cadastro de aluno feito com sucesso",
            "aluno":{
                "id":novo_id,
                "nome":aluno.nome,
                "telefone":aluno.telefone,
                "data_nascimento":aluno.data_nascimento
            }}
#---------------------------
#ROTA ATUALIZA O ALUNO
#---------------------------
@router.put("/alunos/{id}", tags=["Alunos"])
def editar_aluno(id: int, aluno:Aluno):
   conn = conectar()
   cursor = conn.cursor()

   cursor.execute("""UPDATE alunos
                     SET nome = ?,telefone = ?,data_nascimento = ?
                     WHERE id = ?""",(aluno.nome,aluno.telefone,aluno.data_nascimento.strftime("%Y-%m-%d"),id))
   conn.commit()
   conn.close()

   return{"mesagem":"Atualização de aluno ok",
          "alunos":{
              "id":id,
              "nome":aluno.nome,
              "telefone":aluno.telefone,
              "data_nascimento":aluno.data_nascimento}
          }
#----------------------------------
#ROTA DELETE
#----------------------------------
@router.delete("/alunos/{id}", tags=["Alunos"])
def deletar_aluno(id:int):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""DELETE FROM alunos
                      WHERE id = ?""",(id,))
    
    if cursor.rowcount == 0:
     return{
        "mensagem":"Aluno não cadastrado",
        "id":id
        }
    conn.commit()
    conn.close()

    return{
        "mensagem":"Aluno deletado com sucesso",
        "aluno":{
            "id":id,
            
        }
    }