from pydantic import BaseModel
from typing import Optional
class AlunoP(BaseModel):
    id_aluno: int
    email: str
    nome: str
    data_nascimento: float
    cpf: float
    endereco: str
    turma_id: Optional[int]
    
    class Config:
        from_attributes: True

class TurmaP(BaseModel):
    id_turma:int
    alunos: dict
    ano: str
    turno: str
    
    class Config:
        from_attributes: True

class ProfessorP(BaseModel):
    id_professor: int
    nome: str
    
    class Config:
        from_attributes: True

class AlunoUpdate(BaseModel):
    email: Optional[str]
    nome: Optional[str]
    data_nascimento: Optional[float]
    cpf: Optional[float]
    endereco: Optional[str]