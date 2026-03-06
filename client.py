import socket
import hashlib
import secrets
from pathlib import Path
from config import HOST, PORT, BLOCK_SIZE

# Lire le message
msg = Path("data/message.txt").read_text(encoding="utf-8")
print(" Message à envoyer :")
print(msg)

# Générer un nonce UNIQUE (32 caractères hexadécimaux)
nonce = secrets.token_hex(16)
print(f"\n Nonce généré : {nonce}")

# Concaténer nonce + message et calculer le hash
message_with_nonce = nonce + msg
msg_bytes = message_with_nonce.encode("utf-8")
hash_hex = hashlib.sha256(msg_bytes).hexdigest()
print(f" Hash SHA-256 : {hash_hex}")

# Formater le message à envoyer : "hash:nonce:message"
msg_a_envoyer = f"{hash_hex}:{nonce}:{msg}".encode("utf-8")
print(f"\n Paquet à envoyer : {len(msg_a_envoyer)} octets")

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.sendto(msg_a_envoyer, (HOST, PORT))
    print(f" Paquet envoyé à {HOST}:{PORT}")
    
    # Attendre la réponse
    data, _ = s.recvfrom(BLOCK_SIZE)
    reponse = data.decode("utf-8")
    print(f"  Réponse du serveur : {reponse}")
