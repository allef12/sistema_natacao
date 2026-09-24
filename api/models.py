from datetime import date
from typing import Optional
from pydantic import BaseModel, Field
from enum import Enum

class Aluno(BaseModel):
    nome: str
    telefone: Optional[str] = None
    data_nascimento: date
    

class Pagamento(BaseModel):
    aluno_id: int
    mes: str = Field(min_length=3, max_length=20)
    valor:float = Field(gt=0)
    

class StatusPagamento(str, Enum):
    pago = "Pago"
    pendente = "Pendente"
    