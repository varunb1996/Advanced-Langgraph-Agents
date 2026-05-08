import json
from pathlib import Path

MEMORY_FILE = Path("memory/memory.json")

def load_memory():

    if MEMORY_FILE.exists():

        with open(MEMORY_FILE, "r") as f:
            return json.load(f)

    return []

def save_memory(data):

    with open(MEMORY_FILE, "w") as f:
        json.dump(data, f, indent=2)