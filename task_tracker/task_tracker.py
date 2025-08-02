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


