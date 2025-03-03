import json
import os

MEMORY_FILE = "brainwave_memory.json"

# Initialize Memory System
if not os.path.exists(MEMORY_FILE):
    with open(MEMORY_FILE, "w") as file:
        json.dump({}, file)

# Save Memory
def save_memory(question, answer):
    with open(MEMORY_FILE, "r") as file:
        memory = json.load(file)

    memory[question] = answer

    with open(MEMORY_FILE, "w") as file:
        json.dump(memory, file, indent=4)

# Get Memory
def get_memory():
    with open(MEMORY_FILE, "r") as file:
        memory = json.load(file)
    return memory

# Clear Memory
def clear_memory():
    with open(MEMORY_FILE, "w") as file:
        json.dump({}, file)
