import argparse
from asyncio import tasks
import json
import os

file_tasks = "tasks.json"

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
    tasks.append({"descricao": description, "concluida": False})
    save_tasks(tasks)
    print(f"Tarefa adicionada: {description}")

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("Nenhuma tarefa encontrada.")
        return
    for i, tks in enumerate(tasks, 1):
        status = "concluída" if tks["concluida"] else "pendente"
        print(f"{i}. {t['descricao']} - {status}")
        
def complete_task(index):
    tasks = load_tasks()
    if 0 < index <= len(tasks):
        removed_task = tasks.pop(index - 1)
        save_tasks(tasks)
        print(f"Tarefa concluída: {removed_task['descricao']}")
    else:
        print("Índice inválido.")

def delete_task(index):
    tasks = load_tasks()
    if 0 < index <= len(tasks):
        removed_task = tasks.pop(index - 1)
        save_tasks(tasks)
        print(f"Tarefa removida: {removed_task['descricao']}")
    else:
        print("Índice inválido.")
