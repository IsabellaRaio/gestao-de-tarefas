# TechFlow Solutions - Sistema de Gerenciamento de Tarefas

Este projeto consiste no desenvolvimento de um sistema básico de gerenciamento de tarefas (CRUD) voltado para uma startup de logística. O objetivo é permitir o acompanhamento do fluxo de trabalho em tempo real, a priorização de tarefas críticas e o monitoramento do desempenho da equipe por meio de práticas modernas de Engenharia de Software e metodologias ágeis.

---

## Escopo Inicial do Projeto

O sistema é uma API robusta e simplificada construída em Python (FastAPI), que permite:
* **Criar tarefas** com título, descrição e status de progresso.
* **Visualizar tarefas** pendentes e concluídas.
* **Atualizar o status** ou detalhes de tarefas existentes.
* **Deletar tarefas** que não são mais necessárias.

---

## Metodologia Ágil

Para a gestão e acompanhamento do ciclo de vida de desenvolvimento, adotei o framework **Kanban**. 
O progresso das tarefas está mapeado no quadro interativo do **GitHub Projects** utilizando as seguintes colunas:
1. **To Do (A Fazer):** Tarefas aguardando início.
2. **In Progress (Em Progresso):** Tarefas sendo desenvolvidas no momento.
3. **Done (Concluído):** Tarefas que passaram por testes e foram finalizadas.

---

## Tecnologias Utilizadas

* **Linguagem Principal:** Python 3.10+
* **Framework Web:** FastAPI (construção das rotas do CRUD)
* **Testes Automatizados:** Pytest (garantia da qualidade de software)
* **Integração Contínua (CI):** GitHub Actions (automação de testes em cada push)

---

## Como Executar o Projeto Localmente

Siga o passo a passo abaixo para rodar o projeto na sua máquina:

### 1. Clonar o repositório
```bash
git clone [https://github.com/seu-usuario/gestao-de-tarefas.git](https://github.com/seu-usuario/gestao-de-tarefas.git)
cd gestao-de-tarefas