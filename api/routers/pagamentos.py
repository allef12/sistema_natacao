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

#TESTE 
