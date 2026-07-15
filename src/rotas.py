from fastapi import APIRouter, status, HTTPException
from typing import List
from src.modelos import Tarefa, TarefaCriar

router = APIRouter()

db_tarefas: List[Tarefa] = []
id_controlador = 1

@router.post("/tarefas", response_model=Tarefa, status_code=status.HTTP_201_CREATED)
def criar_tarefa(tarefa: TarefaCriar):
    global id_controlador
    nova_tarefa = Tarefa(
        id=id_controlador,
        titulo=tarefa.titulo,
        descricao=tarefa.descricao,
        status=tarefa.status,
        prioridade=tarefa.prioridade  # Adicionado aqui
    )
    db_tarefas.append(nova_tarefa)
    id_controlador += 1
    return nova_tarefa

@router.get("/tarefas", response_model=List[Tarefa])
def listar_tarefas():
    return db_tarefas

@router.get("/tarefas/{tarefa_id}", response_model=Tarefa)
def obter_tarefa(tarefa_id: int):
    for tarefa in db_tarefas:
        if tarefa.id == tarefa_id:
            return tarefa
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, 
        detail="Tarefa não encontrada."
    )

@router.put("/tarefas/{tarefa_id}", response_model=Tarefa)
def atualizar_tarefa(tarefa_id: int, tarefa_atualizada: TarefaCriar):
    for index, tarefa in enumerate(db_tarefas):
        if tarefa.id == tarefa_id:
            tarefa_editada = Tarefa(
                id=tarefa_id,
                titulo=tarefa_atualizada.titulo,
                descricao=tarefa_atualizada.descricao,
                status=tarefa_atualizada.status,
                prioridade=tarefa_atualizada.prioridade  # Adicionado aqui
            )
            db_tarefas[index] = tarefa_editada
            return tarefa_editada
            
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, 
        detail="Tarefa não encontrada para atualização."
    )

@router.delete("/tarefas/{tarefa_id}", status_code=status.HTTP_204_NO_CONTENT)
def deletar_tarefa(tarefa_id: int):
    for index, tarefa in enumerate(db_tarefas):
        if tarefa.id == tarefa_id:
            db_tarefas.pop(index)
            return
            
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, 
        detail="Tarefa não encontrada para exclusão."
    )