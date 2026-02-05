import socket
import hashlib
from pathlib import Path

HOST = "127.0.0.1"
PORT = 12345

# Lire le message original
msg = Path("data/message.txt").read_text(encoding="utf-8")
print("📝 Message original :")
print(msg)

# Encoder en octets
msg_bytes = msg.encode("utf-8")
print(f"\n📦 Encodage UTF-8 : {len(msg_bytes)} octets")

# CORROMPRE 1 BIT : inverser le 10ème bit du message (index 9)
position_bit = 9
position_octet = position_bit // 8
position_dans_octet = position_bit % 8
masque = 1 << (7 - position_dans_octet)

# Créer une copie mutable et corrompre
msg_corrompu = bytearray(msg_bytes)
msg_corrompu[position_octet] ^= masque

print(f"\n CORRUPTION : bit #{position_bit} inversé")
print(f"   Octet #{position_octet} : {msg_bytes[position_octet]} → {msg_corrompu[position_octet]}")

# Hash du message ORIGINAL (celui qu'on prétend envoyer)
hash_original = hashlib.sha256(msg_bytes).hexdigest()

# Envoyer : hash_original + message CORROMPU (pour tromper le serveur)
msg_a_envoyer = f"{hash_original}:{msg_corrompu.decode('utf-8', errors='replace')}".encode("utf-8")

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.sendto(msg_a_envoyer, (HOST, PORT))
    print(f"\n Message CORROMPU envoyé ({len(msg_a_envoyer)} octets)")
    
    # Recevoir la réponse
    data, _ = s.recvfrom(1024)
    print(f"  Réponse du serveur : {data.decode('utf-8')}")