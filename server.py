import socket

HOST = "127.0.0.1"
PORT = 12345

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))
    print(f"✓ Serveur UDP démarré sur {HOST}:{PORT}")
    print("En attente de messages...\n")
    
    while True:
        data, addr = s.recvfrom(1024)
        print(f"📨 Reçu {len(data)} octets de {addr}")
        print(f"   Message : {data.decode('utf-8', errors='replace')}")
        
        reponse = f"✓ Message reçu ({len(data)} octets)"
        s.sendto(reponse.encode("utf-8"), addr)
        print(f"   ↩️  Accusé envoyé à {addr}\n")