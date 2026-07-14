from fastapi import FastAPI
from src.rotas import router as tarefas_router

# Inicializa o aplicativo FastAPI
app = FastAPI(
    title="TechFlow - Sistema de Gerenciamento de Tarefas",
    description="API desenvolvida para controle de fluxo de trabalho e logística.",
    version="1.0.0"
)

# Inclui as rotas de tarefas no aplicativo
app.include_router(tarefas_router)

@app.get("/")
def home():
    return {"status": "API rodando com sucesso! Acesse /docs para ver a documentação."}