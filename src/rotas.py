from fastapi import APIRouter, status
from typing import List
from src.modelos import Tarefa, TarefaCriar

router = APIRouter()

# Banco de dados simulado em memória (uma lista de tarefas)
db_tarefas: List[Tarefa] = []
id_controlador = 1

@router.post("/tarefas", response_model=Tarefa, status_code=status.HTTP_201_CREATED)
def criar_tarefa(tarefa: TarefaCriar):
    """
    Rota para criar uma nova tarefa de logística no sistema (o 'C' do CRUD).
    Recebe os dados da tarefa, gera um ID automático e a salva na memória.
    """
    global id_controlador
    
    nova_tarefa = Tarefa(
        id=id_controlador,
        titulo=tarefa.titulo,
        descricao=tarefa.descricao,
        status=tarefa.status
    )
    
    db_tarefas.append(nova_tarefa)
    id_controlador += 1
    return nova_tarefa