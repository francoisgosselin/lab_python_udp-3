import socket
import hashlib
import secrets
from pathlib import Path

HOST = "127.0.0.1"
PORT = 12345

# Lire le message
msg = Path("data/message.txt").read_text(encoding="utf-8")

# Générer UN SEUL nonce (pour les 2 envois)
nonce = secrets.token_hex(16)
print(f"🔑 Nonce UNIQUE : {nonce}")

# Créer le paquet UNE FOIS
message_with_nonce = nonce + msg
hash_hex = hashlib.sha256(message_with_nonce.encode("utf-8")).hexdigest()
paquet = f"{hash_hex}:{nonce}:{msg}".encode("utf-8")

# Envoyer 2 fois le MÊME paquet
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    print("\n🚀 Envoi 1/2 (légitime)...")
    s.sendto(paquet, (HOST, PORT))
    print(f"↩️  Réponse : {s.recvfrom(1024)[0].decode('utf-8')}")
    
    print("\n🚀 Envoi 2/2 (ATTAQUE PAR REJEU !)...")
    s.sendto(paquet, (HOST, PORT))
    print(f"↩️  Réponse : {s.recvfrom(1024)[0].decode('utf-8')}")