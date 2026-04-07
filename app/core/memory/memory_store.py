import json
import os
from typing import TypedDict 

MEMORY_FILE = "C:/Users/Administrador/OneDrive/Documentos/Projects/007_osrs_multi_agent/app/core/memory/memory.json"

class MemoryStore:

    def __init__(self):
        if not os.path.exists("MEMORY_FILE"):
            with open(MEMORY_FILE, "w") as f:
                json.dump({}, f)
    
    def load(self, session_id: str) -> TypedDict:
        with open(MEMORY_FILE, "r") as f:
            data = json.load(f)

        return data.get(session_id, {})
    
    def save(self, session_id: str, state: TypedDict):
        with open(MEMORY_FILE, "r") as f:
            data = json.load(f)

        data[session_id] = state

        with open(MEMORY_FILE, "w") as f:
            json.dump(data, f, indent=2)