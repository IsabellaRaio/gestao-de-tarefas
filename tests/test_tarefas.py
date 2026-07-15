from fastapi.testclient import TestClient
from src.main import app
from src.rotas import db_tarefas

client = TestClient(app)

def setup_function():
    db_tarefas.clear()

def test_criar_tarefa_com_sucesso():
    payload = {
        "titulo": "Entregar carga de insumos",
        "descricao": "Rota expressa.",
        "status": "To Do",
        "prioridade": "Alta"  # Testando a nova propriedade
    }
    response = client.post("/tarefas", json=payload)
    
    assert response.status_code == 201
    dados = response.json()
    assert dados["titulo"] == payload["titulo"]
    assert dados["prioridade"] == "Alta"
    assert "id" in dados

def test_criar_tarefa_sem_titulo_retorna_erro():
    payload = {
        "titulo": "",
        "descricao": "Sem título.",
        "status": "To Do"
    }
    response = client.post("/tarefas", json=payload)
    assert response.status_code == 422

def test_listar_tarefas_cadastradas():
    client.post("/tarefas", json={"titulo": "Tarefa de Teste", "status": "In Progress"})
    response = client.get("/tarefas")
    assert response.status_code == 200
    dados = response.json()
    assert len(dados) == 1
    assert dados[0]["prioridade"] == "Média"  # Deve vir o valor padrão "Média"

def test_buscar_tarefa_por_id_inexistente_retorna_404():
    response = client.get("/tarefas/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Tarefa não encontrada."