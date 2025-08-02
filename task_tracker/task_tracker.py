import argparse
from hmac import new
import json
import os

from datetime import datetime

file_tasks = "tasks.json"

def now():
    return datetime.now().isoformat(timespec="seconds")

def load_tasks():
    if os.path.exists(file_tasks):
        with open(file_tasks, 'r') as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(file_tasks, 'w') as file:
        json.dump(tasks, file, indent=4)


def add_task(description):
    tasks = load_tasks()
    taks_id = max([tks["id"] for tks in tasks], default=0) + 1
    new_tasks = {
        "id": taks_id,
        "description": description,
        "status": "todo",
        "createdAt": now(),
        "updateAt": now()
    }
    tasks.append(new_tasks)
    save_tasks(tasks)
    print(f"Tarefa adicionada: {description}")

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("Nenhuma tarefa encontrada.")
        return
    for tks in tasks:
        print(f"{tks['id']}. {tks['description']} - {tks['status']} | Criada em: {tks['createdAt']} - Atualizada em: {tks['updateAt']}")
        
def complete_task(index):
    tasks = load_tasks()
    if 0 < index <= len(tasks):
        tasks[index - 1]["concluida"] = True
        save_tasks(tasks)
        print(f"Tarefa marcada como concluída: {tasks[index - 1]['descricao']}")
    else:
        print("Índice inválido")

def delete_task(index):
    tasks = load_tasks()
    if 0 < index <= len(tasks):
        removed_task = tasks.pop(index - 1)
        save_tasks(tasks)
        print(f"Tarefa removida: {removed_task['descricao']}")
    else:
        print("Índice inválido.")

def main():
    parser = argparse.ArgumentParser(description="Rastreador de tarefas (CLI)")
    subparsers = parser.add_subparsers(dest="command")

    # Adicionar tarefa
    parser_add = subparsers.add_parser("add", help="Adicionar uma nova tarefa")
    parser_add.add_argument("description", type=str, help="Descrição da tarefa")

    # Listar tarefas
    subparsers.add_parser("list", help="Listar todas as tarefas")

    # Concluir tarefa
    parser_complete = subparsers.add_parser("complete", help="Concluir uma tarefa")
    parser_complete.add_argument("index", type=int, help="Índice da tarefa a ser concluída")

    # Remover tarefa
    parser_delete = subparsers.add_parser("delete", help="Remover uma tarefa")
    parser_delete.add_argument("index", type=int, help="Índice da tarefa a ser removida")

    args = parser.parse_args()

    match args.command:
        case "add":
            add_task(args.description)
        case "list":
            list_tasks()
        case "complete":
            complete_task(args.index)
        case "delete":
            delete_task(args.index)
        case _:
            parser.print_help()

if __name__ == "__main__":
    main()