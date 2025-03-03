import hashlib

# Vault Password Encryption
def encrypt_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Vault Lock System
VAULT_PASSWORD = encrypt_password("brainwavevault")

def unlock_vault(password):
    if encrypt_password(password) == VAULT_PASSWORD:
        return True
    return False

# Hidden Chat Locker
hidden_chats = []

def add_hidden_chat(chat):
    hidden_chats.append(chat)

def get_hidden_chats():
    return hidden_chats

# App Lock System
def app_lock(password):
    return unlock_vault(password)
