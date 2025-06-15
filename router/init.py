from fastapi import APIRouter
import json

router = APIRouter()

@router.get('/ids')
def retornar_ids():
    arquivos = ['alunos.json', 'professores.json', 'turmas.json']
    ids = []

    for arquivo in arquivos:
        with open(arquivo, 'r') as f:
            data = json.load(f)
            ids = [item['id'] for item in data]
            ids.extend(ids)
   
    id_unico = list(set(ids))

    return {"ids": id_unico}