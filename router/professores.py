from fastapi import APIRouter, HTTPException
from models import Professores, AtribuirProfessor
from models import salvar_dados, carregar_dados

router = APIRouter(prefix='/professores', tags=['Professores'])

@router.post("/")
def cadastrar_professores(professor: Professores):
    professores = carregar_dados('professores.json') or []

    if any(p['id'] == professor.id for p in professores):
        raise HTTPException(status_code=400, detail=f'O professor está com o ID {professor.id} já está cadastrado com sucesso')

    professores.append(professor.dict())
    salvar_dados('professores.json', professores)

    return {"mensagem": f"Professor {professor.nome} com ID {professor.id} foi cadastrado com sucesso!"}

# EDITAR PROFESSORES:
@router.put("/{id_professor}")
def editar_professor(id_professor: int, dados_professores: dict):
    professores = carregar_dados('professores.json') or []

    for professor in professores:
        if professor['id'] == id_professor:
            professor.update(dados_professores)
            salvar_dados('professores.json', professores)
            return {'mensagem': "Professor {id_professor} atualizado com sucesso"}

    raise HTTPException(status_code=400, detail='Professor não encontrando!')

# DELETAR PROFESSORES:
@router.delete("/{id_professor}")
def deleter_professor(id_professor: int):
    professores = carregar_dados('professor.json') or []
    novos_professores = [p for p in professores if p['id'] != id_professor]

    if len(professores) == len(novos_professores):
        raise HTTPException(status_code=400, detail='Professor não encontrado')
    
    salvar_dados('professores.json', novos_professores)
    return {'mensagem': f'Professor {id_professor} deletado com sucesso!'}


# LISTAR PROFESSORES:
@router.get("/")
def listar_professores():
    professores = carregar_dados('professores.json') or []
    return professores
    
# ATRIBUIR PROFESSORES A TURMAS

@router.post("/atribuir")
def atribuir_professor(dados: AtribuirProfessor):
   professores = carregar_dados('professores.json') or []
   turmas = carregar_dados('turmas.json') or []
   atribuicoes = carregar_dados('professores_turmas.json') or []

   if not any(p['id'] == dados.id_professor for p in professores):
    raise HTTPException(status_code=400, detail='Professor não encontrado')

   if not any (t['id'] == dados.id_turma for t in turmas):
    raise HTTPException(status_code=400, detail='Turmas não encontrada')

   if any(
        a['id_professor'] == dados.id_professor and a['id_turma'] == dados.id_turma
        for a in atribuicoes
    ):
        return {"mensagem": "Professor já está atribuído a essa turma"}

   atribuicoes.append({
        "id_professor": dados.id_professor,
        "id_turma": dados.id_turma
    })
   salvar_dados('professores_turmas.jsos', atribuicoes)
   return {"mensagem": f"Professor {dados.id_professor} atribuído à turma {dados.id_turma}"}

   # LISTAR ATRIBUICOES:
@router.get('/atribuicoes')
def listar_atribuicoes():
    atribuicoes = carregar_dados('professores_turmas.json') or []
    return atribuicoes
    
