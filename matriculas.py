from fastapi import APIRouter, HTTPException
from models import MatriculaAluno, carregar_dados, salvar_dados

router = APIRouter(prefix="/matriculas", tags=["Matriculas"])

@router.post("/")
def matricular_aluno(dados: MatriculaAluno):
    alunos = carregar_dados('alunos.json') or []
    turmas = carregar_dados('turmas.json') or []
    alunos_turmas = carregar_dados('alunos_turmas.json') or {}

    # Verificar se aluno existe
    if not any(a['id'] == dados.id_aluno for a in alunos):
        raise HTTPException(status_code=404, detail="Aluno não encontrado")

    # Verificar se turma existe
    if not any(t['id'] == dados.id_turma for t in turmas):
        raise HTTPException(status_code=404, detail="Turma não encontrada")

    # Matricular
    if str(dados.id_aluno) not in alunos_turmas:
        alunos_turmas[str(dados.id_aluno)] = []

    if dados.id_turma in alunos_turmas[str(dados.id_aluno)]:
        return {"mensagem": "Aluno já matriculado nesta turma"}

    alunos_turmas[str(dados.id_aluno)].append(dados.id_turma)
    salvar_dados('alunos_turmas.json', alunos_turmas)

    return {"mensagem": f"Aluno {dados.id_aluno} matriculado na turma {dados.id_turma}"}
