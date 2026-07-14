from fastapi.testclient import TestClient
from src.main import app
from src.rotas import db_tarefas

# Inicializa o cliente de testes da FastAPI (usa o HTTPX por baixo dos panos)
client = TestClient(app)

def setup_function():
    """
    Função executada automaticamente antes de cada teste individual.
    Ela garante que o nosso 'banco de dados' em memória seja limpo,
    evitando que um teste interfira no resultado do outro.
    """
    db_tarefas.clear()

def test_criar_tarefa_com_sucesso():
    """
    Testa se a rota POST cria uma tarefa corretamente quando os dados estão válidos.
    """
    payload = {
        "titulo": "Entregar carga de insumos",
        "descricao": "Rota expressa para o centro de distribuição.",
        "status": "To Do"
    }
    response = client.post("/tarefas", json=payload)
    
    assert response.status_code == 201
    dados = response.json()
    assert dados["titulo"] == payload["titulo"]
    assert dados["descricao"] == payload["descricao"]
    assert dados["status"] == "To Do"
    assert "id" in dados

def test_criar_tarefa_sem_titulo_retorna_erro():
    """
    Testa a validação do Pydantic. Tentar criar uma tarefa com título em branco
    deve retornar um erro 422 (Unprocessable Entity).
    """
    payload = {
        "titulo": "",  # Título inválido (min_length=1)
        "descricao": "Sem título.",
        "status": "To Do"
    }
    response = client.post("/tarefas", json=payload)
    assert response.status_code == 422

def test_listar_tarefas_cadastradas():
    """
    Testa se a rota GET retorna a lista correta de tarefas.
    """
    # Cria uma tarefa manualmente para o teste
    client.post("/tarefas", json={"titulo": "Tarefa de Teste", "status": "In Progress"})
    
    response = client.get("/tarefas")
    assert response.status_code == 200
    dados = response.json()
    assert len(dados) == 1
    assert dados[0]["titulo"] == "Tarefa de Teste"

def test_buscar_tarefa_por_id_inexistente_retorna_404():
    """
    Testa se o sistema retorna erro 404 ao buscar por um ID que não existe.
    """
    response = client.get("/tarefas/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Tarefa não encontrada."