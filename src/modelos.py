from pydantic import BaseModel, Field
from typing import Optional

class TarefaCriar(BaseModel):
    titulo: str = Field(..., min_length=1)
    descricao: Optional[str] = None
    status: str = "To Do"
    prioridade: str = "Média"  # Novo campo adicionado na mudança de escopo!

class Tarefa(TarefaCriar):
    id: int