from datetime import date
from typing import Optional
from pydantic import BaseModel,  field_validator, Field
from enum import Enum

class Aluno(BaseModel):
    nome: str
    telefone: Optional[str] = None
    data_nascimento: date
    

class Pagamento(BaseModel):
    

class StatusPagamento(str, Enum):
    pago = "Pago"
    pendente = "Pendente"

