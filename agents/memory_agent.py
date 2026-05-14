from tools.memory_tool import (
    load_memory,
    save_memory
)

def memory_agent(state):

    memory = load_memory()

    memory.append({
        "query": state["query"]
    })

    save_memory(memory)

    state["memory"] = memory[-5:]

    return state