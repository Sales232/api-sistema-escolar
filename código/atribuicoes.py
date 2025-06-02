from fastapi import APIRouter, HTTPException
from models import AtribuirProfessor, carregar_dados, salvar_dados

router = APIRouter(prefix="/atribuicoes", tags=["Atribuições"])

@router.post("/")
def atribuir_professor(dados: AtribuirProfessor):
    professores = carregar_dados('professores.json') or []
    turmas = carregar_dados('turmas.json') or []
    professores_turmas = carregar_dados('professores_turmas.json') or {}

    # Verificar se professor existe
    if not any(p['id'] == dados.id_professor for p in professores):
        raise HTTPException(status_code=404, detail="Professor não encontrado")

    # Verificar se turma existe
    if not any(t['id'] == dados.id_turma for t in turmas):
        raise HTTPException(status_code=404, detail="Turma não encontrada")

    if str(dados.id_professor) not in professores_turmas:
        professores_turmas[str(dados.id_professor)] = []

    if dados.id_turma in professores_turmas[str(dados.id_professor)]:
        return {"mensagem": "Professor já atribuído a esta turma"}

    professores_turmas[str(dados.id_professor)].append(dados.id_turma)
    salvar_dados('professores_turmas.json', professores_turmas)

    return {"mensagem": f"Professor {dados.id_professor} atribuído à turma {dados.id_turma}"}
