from datetime import date
import re
from pydantic import BaseModel,  field_validator, Field
from enum import Enum

class Aluno(BaseModel):
  nome:str
  telefone:str
  data_nascimento:date

  @field_validator("telefone")
  @classmethod
  def validar_telefone(cls,valor):
      apenas_numeros = re.sub(r"\D","",valor)
      
      if len(apenas_numeros) not in(10, 11):
          raise ValueError("O número tem que ter 10 ou 11 dígitos com (DDD)")
      
      return valor

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

