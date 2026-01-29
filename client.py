import socket
from pathlib import Path

HOST = "127.0.0.1"
PORT = 12345

msg = Path("data/message.txt").read_text(encoding="utf-8")
print("📝 Message à envoyer :")
print(msg)

msg_bytes = msg.encode("utf-8")
print(f"\n📦 Encodage UTF-8 : {len(msg)} caractères → {len(msg_bytes)} octets")

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.sendto(msg_bytes, (HOST, PORT))
    print(f"✅ Message envoyé à {HOST}:{PORT}")
    
    data, _ = s.recvfrom(1024)
    reponse = data.decode("utf-8")
    print(f"↩️  Réponse du serveur : {reponse}")