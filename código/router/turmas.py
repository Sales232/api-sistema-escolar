from fastapi import APIRouter, HTTPException
from models import Turmas
from models import salvar_dados, carregar_dados

router = APIRouter(prefix='/turmas', tags=['Turmas'])

# CADASTRAR TURMAS:
@router.post("/")
def cadastrar_turma(turma: Turmas):
    turmas = carregar_dados('turmas.json') or []

    if any(t['id'] == turma.id for t in turmas):
        raise HTTPException( status_code=400, detail=f'A turma {turma.id} já está cadastrada'
        )
    turmas.append(turma.dict())
    salvar_dados('turmas.json', turmas)
    return {'mensagem': f'A turma {turma.nome} já está cadastrada'}

# LISTAR AS TURMAS
@router.get("/")
def listar_turmas():
    turmas = carregar_dados('turmas.json') or []
    return turmas

# EDITAR AS TURMAS:
@router.put("/{id_turma}")
def editar_turma(id_turma: int, dados_turma: dict):
    turmas = carregar_dados('turmas.json') or []
    for turma in turmas:
        if turma['id'] == id_turma:
            turma.update(dados_turma)
            salvar_dados('turmas.json', turmas)
            return {"mensagem": f'Turma {id_turma} castrada com sucesso'}
    raise HTTPException(status_code=400, detail='Turma ão encontrada')

# DELETAR A TURMA:
@router.delete('/{id_turma}')
def deletar_turma(id_turma: int):
    turmas = carregar_dados('turmas.json')
    novas_turmas = [t for t in turmas if t['id'] != id_turma]
    if len(turmas) == len(novas_turmas):
        raise HTTPException(status_code=400, detail='Turma não encontrada')
    salvar_dados('turmas.json', novas_turmas)
    return {'mensagem': f'Turma {id_turma} deletada com sucesso'}
     