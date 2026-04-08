# README.md

O projeto segue uma arquitetura em camadas:

```
├── tasks_fastapi_app.py    # Entry point: inicializa o FastAPI e registra os routers
├── model/
│   └── task.py             # Modelos Pydantic: Task, TaskInput, TaskUpdate
├── router/
│   └── task_router.py      # Rotas HTTP (GET, POST, PUT, DELETE) em /todo/api/tasks
└── dao/
    └── task_dao.py         # Acesso a dados — ÚNICA camada a ser modificada
```

### Modelos de dados

- `Task` — representação completa da tarefa (campos: `id`, `title`, `description`, `done`)
- `TaskInput` — payload de criação (sem `id`)
- `TaskUpdate` — todos os campos opcionais, usado no PUT para atualização parcial

### Endpoints disponíveis

| Método | Rota | Descrição |
|--------|------|-----------|
| `GET` | `/todo/api/tasks/` | Lista todas as tarefas |
| `GET` | `/todo/api/tasks/{task_id}` | Busca tarefa por ID |
| `POST` | `/todo/api/tasks/` | Cria nova tarefa |
| `PUT` | `/todo/api/tasks/{task_id}` | Atualiza tarefa existente |
| `DELETE` | `/todo/api/tasks/{task_id}` | Remove tarefa |