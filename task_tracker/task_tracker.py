import argparse
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
        "updatedAt": now()
    }
    tasks.append(new_tasks)
    save_tasks(tasks)
    print(f"Tarefa adicionada: {description}")

def list_tasks(status=None):
    tasks = load_tasks()
    if status:
        tasks = [tks for tks in tasks if tks["status"] == status]
        if not tasks:
            print(f"Nenhuma tarefa com status '{status}'.")
            return
        print(f"Tarefas com status '{status}':")
    else:
        if not tasks:
            print("Nenhuma tarefa encontrada.")
            return
    for tks in tasks:
        print(f"{tks['id']}. {tks['description']} - {tks['status']} | Criada em: {tks['createdAt']} - Atualizada em: {tks['updatedAt']}")

def mark_status_tasks(task_id, status):
    valid_status = {"todo", "in_progress", "done"}
    if status not in valid_status:
        print(f"Status inválido. Escolha entre: {', '.join(valid_status)}")
        return
    
    tasks = load_tasks()

    for tks in tasks:
        if tks["id"] == task_id:
            tks["status"] = status
            tks["updatedAt"] = now()
            save_tasks(tasks)
            print(f"Tarefa atualizada: {tks['description']} -- status: '{status}'")
            return
    print("ID inválido")

def update_task(task_id, new_description):
    tasks = load_tasks()
    for tks in tasks:
        if tks["id"] == task_id:
            tks["description"] = new_description
            tks["updatedAt"] = now()
            save_tasks(tasks)
            print(f"Descrição atualizada: {new_description}")
            return
    print("ID inválido")

def delete_task(task_id):
    tasks = load_tasks()
    for idx, tks in enumerate(tasks):
        if tks["id"] == task_id:
            removed = tasks.pop(idx)
            save_tasks(tasks)
            print(f"Tarefa removida: {removed['description']}")
            return
    print("ID inválido")

def main():
    parser = argparse.ArgumentParser(description="Rastreador de tarefas (CLI)")
    subparsers = parser.add_subparsers(dest="command")

    parser_add = subparsers.add_parser("add", help="Adicionar uma nova tarefa")
    parser_add.add_argument("description", type=str, help="Descrição da tarefa")

    parser_list = subparsers.add_parser("list", help="Listar tarefas")
    parser_list.add_argument("--status", type=str, choices=["todo", "in_progress", "done"], help="Filtrar tarefas por status")

    parser_mark = subparsers.add_parser("mark", help="Atualizar status de uma tarefa")
    parser_mark.add_argument("id", type=int, help="Índice da tarefa a ser atualizada com status")
    
    parser_delete = subparsers.add_parser("delete", help="Remover uma tarefa")
    parser_delete.add_argument("id", type=int, help="Índice da tarefa a ser removida")

    parser_update = subparsers.add_parser("update", help="Atualizar descrição da tarefa")
    parser_update.add_argument("id", type=int, help="Índice da tarefa a ser atualizada")
    parser_update.add_argument("description", type=str, help="Nova descrição da tarefa")

    args = parser.parse_args()

    match args.command:
        case "add":
            add_task(args.description)
        case "list":
            list_tasks(args.status)
        case "mark":
            mark_status_tasks(args.id, "in_progress")
        case "delete":
            delete_task(args.id)
        case "update":
            update_task(args.id, args.description)
        case _:
            parser.print_help()

if __name__ == "__main__":
    main()