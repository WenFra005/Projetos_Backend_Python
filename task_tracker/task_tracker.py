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

