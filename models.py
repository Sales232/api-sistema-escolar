from pydantic import BaseModel
from typing import Optional
import json
import os

class Aluno(BaseModel):
    id_aluno: int
    nome: str
    data_nascimento: str
    cpf_pais: str
    endereco: str

class Turmas(BaseModel):
    id: int
    nome: str
    ano: int
    turno: str

class Professores(BaseModel):
    id: int
    nome: str

class MatriculaAluno(BaseModel):
    id_aluno: int
    id_turma: int


class AtribuirProfessor(BaseModel):
    id_professor: int
    id_turma: int
    
class AlunoUpdate(BaseModel):
    nome: Optional[str]
    data_nascimento: Optional[str]
    cpf_pais: Optional[str]
    endereco: Optional[str]
    
# banco de dados:
def salvar_dados(nome_arquivo, dados):
    with open(nome_arquivo, 'w', encoding='utf-8') as f:
        json.dump(dados, f, ensure_ascii=False, indent=4)


def carregar_dados(nome_arquivo):
    if not os.path.exists(nome_arquivo):
        return []
    with open(nome_arquivo, 'r', encoding='utf-8') as f:
        return json.load(f)
