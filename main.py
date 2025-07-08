from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models.models import Base, db
import uvicorn

# NOME DA API
app = FastAPI(
    title="Sistema Escolar API",
    description="API voltada ao gerenciamento de sistemas web escolares para rede pública e privada. Está em fase de construção, será voltado ao meu TCC.",
    version= "0.1.0",
)
from router import alunos

Base.metadata.create_all(bind=db)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True, 
    allow_methods=["*"],
    allow_headers=["*"],
)

# ROTAS:

app.include_router(alunos.router)


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)


# FUNCIONAMENTO DA API
@app.get('/')
def mensagem():
    return {"mensagem:" "API FUNCIONANDO!"}

