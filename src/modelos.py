from pydantic import BaseModel, Field
from typing import Optional

class TarefaBase(BaseModel):
    """
    Modelo base que define os campos comuns de uma tarefa.
    """
    titulo: str = Field(
        ..., 
        min_length=1, 
        max_length=100, 
        description="O título da tarefa é obrigatório e deve ter entre 1 e 100 caracteres."
    )
    descricao: Optional[str] = Field(
        None, 
        max_length=500, 
        description="Descrição detalhada sobre a tarefa de logística."
    )
    status: str = Field(
        "To Do", 
        description="Status atual da tarefa (valores esperados: To Do, In Progress, Done)."
    )

class TarefaCriar(TarefaBase):
    """
    Modelo utilizado para receber os dados na criação de uma nova tarefa.
    O ID não é enviado aqui, pois será gerado automaticamente pelo sistema.
    """
    pass

class Tarefa(TarefaBase):
    """
    Modelo completo que representa uma tarefa salva no sistema, incluindo seu ID único.
    """
    id: int