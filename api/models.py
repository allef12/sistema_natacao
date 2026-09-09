from datetime import date
from typing import Optional
from pydantic import BaseModel

class Aluno(BaseModel):
    nome: str
    telefone: Optional[str] = None
    data_nascimento: date
    