from fastapi import APIRouter
from database import conectar 
from models import Pagamento 

router = APIRouter()  
#------------------------------
#ROTA POST
#------------------------------

@router.post("/pagamentos",tags=["Pagamentos"], status_code=201)
def registro_pagamentos(pag:Pagamento,):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""INSERT INTO pagamentos (aluno_id,mes,valor,status) 
                      VALUES(?,?,?,?)""",
                      (pag.aluno_id,pag.mes,pag.valor,"Pago"))

    conn.commit()
    conn.close()

    return{
        "mensagem":"Pagamento registrado com sucesso",
        "pagamento":{"aluno":pag.aluno_id,
                     "mes":pag.mes,
                     "valor":pag.valor,
                     "status":"Pago"}
    }


#-----------------------------
#ROTA GET todos
#-----------------------------

@router.get("/pagamentos",tags=["Pagamentos"])
def listar_todos_pagamentos():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""SELECT p.id,a.nome,p.valor,p.mes,p.status
                      FROM alunos a
                      JOIN pagamentos p ON a.id = p.aluno_id""")

    aluno = cursor.fetchall()

    conn.close()

    return[
        {"id":alunos.id,
         "nome":alunos.nome,
         "valor":alunos.valor,
         "mes":alunos.mes,
         "status":alunos.status
         }
         for alunos in aluno
    ]


#----------------------------------
#ROTA GET pagamento específico
#----------------------------------

@router.get("/pagamentos/{id}",tags=["Pagamentos"])
def pag_especifico(id:int):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""SELECT id,aluno_id,mes,valor,status
                       FROM pagamentos
                       WHERE id = ?""",(id,))
    pagamento = cursor.fetchone()

    conn.close()

    if pagamento is None:
        return{"mensagem":"Pagamento não encontrado"}

    return{
          "id":pagamento.id,
          "aluno_id":pagamento.aluno_id,
          "mes":pagamento.mes,
          "valor":pagamento.valor,
          "status":pagamento.status
         }