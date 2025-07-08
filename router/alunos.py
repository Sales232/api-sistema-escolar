from fastapi import APIRouter, Depends, HTTPException
from models.models import db, Aluno
from models.models_pydantic import AlunoP, AlunoUpdate
from models.dependencias import pegar_sessao
from sqlalchemy.orm import Session
from typing import List


router = APIRouter(prefix='/alunos', tags=['Alunos'])

@router.get("/",  tags=['Alunos'], status_code=200)
async def listar_alunos(session: Session = Depends(pegar_sessao)):
    alunos = session.query(Aluno).all()
    return alunos

@router.post("/", tags=['Alunos'], status_code=201)
async def cadastrar_alunos(aluno: AlunoP, session: Session = Depends(pegar_sessao)):
    """
    Esta rota é a rota responsável por cadastrar seus alunos e salvar no banco de dados os alunos. Você deverá utilizar os parâmetros dê:
    - ID do aluno: criará um ID para o aluno; deve ser um número inteiro; 
    - NOME DO ALUNO: colocará o nome completo do respectivo aluno; deve ser um texto;
    - DATA DE NASCIMENTO: colocará a data de nascimento do aluno; poderá utilizar as "/" (BARRAS para dividir), por isso é um texto;
    - CPF DOS PAIS: colocará o CPF da mãe do aluno; utilizará os "." (pontos finais) para dividir, por isso é um texto;
    - ENDEREÇO DO ALUNO: colocará o endereço do aluno, por isso é uma string. Utilize o exemplo: Rua, Quadra, Lote, cidade-estado
   """
    
    novo_aluno = Aluno(**aluno.dict())
    session.add(novo_aluno)
    session.commit()
    session.refresh(novo_aluno)
    return {'mensagem': f"Aluno {novo_aluno.nome} cadastrado com sucesso!"}

@router.put('/{id}', tags=["Alunos"], response_model=List[AlunoP])
async def editar_aluno(id_aluno: int, aluno: AlunoUpdate, session: Session = Depends(pegar_sessao)):
    # Vai pegar o ID do aluno e filtrar
    alunos = session.query(Aluno).filter(Aluno.id_aluno == id_aluno).first()

    if not aluno:
        raise HTTPException(status_code=400, detail='Aluno não encontrado')
    # Aqui cria as medidas pro banco de dados 
    alunos.nome = aluno.nome
    alunos.email = aluno.email
    alunos.data_nascimento = aluno.data_nascimento
    alunos.cpf = aluno.cpf
    alunos.endereco = aluno.endereco

    session.commit()
    session.refresh(alunos)
    return [alunos]

    
  


