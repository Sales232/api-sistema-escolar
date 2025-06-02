from fastapi import APIRouter, HTTPException
from models import Aluno, MatriculaAluno
from models import salvar_dados, carregar_dados
import json, os

router = APIRouter(prefix='/alunos', tags=['Alunos'])

@router.post("/", tags=['Alunos'])
def cadastrar_alunos(aluno: Aluno):
    alunos = carregar_dados('alunos.json') or []
    for a in alunos:
        if a['id'] == aluno.id:
            raise HTTPException(status_code=400, detail='Aluno já foi cadastrado')

    alunos.append(aluno.dict())
    salvar_dados('alunos.json', alunos)
    return {"mensagem: f' Aluno: {aluno.nome} cadastrado com sucesso!"}


@router.get("/", tags=['Alunos'])
def listar_alunos():
    alunos = carregar_dados('alunos.json') or []
    return alunos


@router.put("/{id_aluno}", tags=['Alunos'])
def editar_aluno(id_aluno: int, dados_aluno: dict):
    alunos = carregar_dados('alunos.json') or []

    for aluno in alunos:
        if aluno['id'] == id_aluno:
            aluno.update(dados_aluno)
            salvar_dados('alunos.json', alunos)
            return {'mensagem': "Aluno atualizado com sucesso"}
    raise HTTPException(status_code=400, detail='Aluno não encontrando!')
@router.delete('/{id_aluno}', tags=['Alunos'])
def excluir_aluno(id_aluno: int):
    alunos = carregar_dados('alunos.json') or []
    novos_alunos = [a for a in alunos if a['id'] != id_aluno]

    if len(novos_alunos) == len(alunos):
        raise HTTPException(status_code=400, detail='Aluno não encontrado')

    salvar_dados('alunos.json', novos_alunos)
    return {'mensagem:' f'Aluno {id_aluno} removido com sucesso'}

@router.post("/matricular", tags=['Alunos'])
def matricular_aluno(dados: MatriculaAluno):
    alunos = carregar_dados('alunos.json') or []
    turmas = carregar_dados('turmas.json') or []
    matriculas = carregar_dados('matriculas.json') or []

    aluno_existe = any(a['id'] == dados.id_aluno for a in alunos)
    turma_existe = any(t['id'] == dados.id_turma for t in turmas)

    if not aluno_existe:
        raise HTTPException(status_code=400, detail='Aluno não encontrado')

    if not turma_existe:
        raise HTTPException(status_code=400, detail='Turma não encontrada')
    
    for m in matriculas:
        if m['id_aluno'] == dados.id_aluno and m['id_turma'] == dados.id_turma:
            return{'mensagem': 'Aluno já matriculado na turma'}

    matriculas.append({
        "id_aluno": dados.id_aluno,
        "id_turma": dados.id_turma
        })
    salvar_dados('matriculas.json', matriculas)
    return{"mensagem": f"Aluno {dados.id_aluno} matriculado na turma {dados.id_turma}"}

@router.get('/matriculas',tags=['Alunos'])
def listar_matriculas():
    matriculas = carregar_dados('matriculas.json') or []
    return matriculas