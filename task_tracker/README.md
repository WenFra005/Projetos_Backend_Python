# Task Tracker CLI

**URL do projeto:** https://github.com/WenFra005/python_backend_projetos/tree/main/task_tracker

Um rastreador de tarefas simples via linha de comando em Python.

## Funcionalidades

- Adicionar tarefas
- Atualizar descrição de tarefas
- Excluir tarefas
- Marcar tarefas como "em andamento", "feito" ou "a fazer"
- Listar todas as tarefas
- Listar tarefas filtrando por status (`todo`, `in_progress`, `done`)

## Como usar

Execute o script principal:

```bash
python task_tracker.py <comando> [opções]
```

### Comandos disponíveis

#### Adicionar tarefa

```bash
python task_tracker.py add "Descrição da tarefa"
```

#### Listar todas as tarefas

```bash
python task_tracker.py list
```

#### Listar tarefas por status

```bash
python task_tracker.py list --status todo
python task_tracker.py list --status in_progress
python task_tracker.py list --status done
```

#### Atualizar descrição de uma tarefa

```bash
python task_tracker.py update <id> "Nova descrição"
```

#### Marcar tarefa como "em andamento"

```bash
python task_tracker.py mark <id>
```

#### Excluir tarefa

```bash
python task_tracker.py delete <id>
```

## Estrutura dos dados

As tarefas são armazenadas em um arquivo `tasks.json` com os campos:

- `id`: identificador único
- `description`: descrição da tarefa
- `status`: `todo`, `in_progress` ou `done`
- `createdAt`: data de criação
- `updatedAt`: data da última atualização

