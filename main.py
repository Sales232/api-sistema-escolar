from fastapi import FastAPI
import uvicorn
from router import alunos, professores, turmas, init
from models import carregar_dados
import os, json

# NOME DA API
app = FastAPI()

# ROTAS:

app.include_router(alunos.router)
app.include_router(professores.router)
app.include_router(turmas.router)
app.include_router(init.router)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)

professores = carregar_dados('professores.json')
alunos = carregar_dados('alunos.json')
turmas = carregar_dados('turmas.json')
professores_turmas = carregar_dados('professores_turmas.json')

# FUNCIONAMENTO DA API
@app.get('/')
def mensagem():
    return {"mensagem:" "API FUNCIONANDO!"}

