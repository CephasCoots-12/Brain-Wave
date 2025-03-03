chat_memory = []

def save_memory(user, response):
    chat_memory.append({"user": user, "bot": response})
    return chat_memory
