from datetime import date
import re
from pydantic import BaseModel,  field_validator, Field
from enum import Enum

class Aluno(BaseModel):
  nome:str
  telefone:str
  data_nascimento:date

    

class Pagamento(BaseModel):
    aluno_id:int
    mes:str
    valor:float = Field(gt=0)

    @field_validator("mes")
    @classmethod
    def validar_mes(cls, valor):
        meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
         "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
            ]
        if valor not in meses:
            raise ValueError("Mês inválido")

        return valor 
    
    

class StatusPagamento(str, Enum):
    pago = "Pago"
    pendente = "Pendente"

