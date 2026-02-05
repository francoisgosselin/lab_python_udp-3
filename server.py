import socket
import hashlib

HOST = "127.0.0.1"
PORT = 12345
used_nonces = set()

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))
    print(f"✓ Serveur UDP sécurisé avec nonce sur {HOST}:{PORT}")
    print("En attente de paquets 'hash:nonce:message'...\n")
    
    while True:
        data, addr = s.recvfrom(2048)
        print(f" Reçu {len(data)} octets de {addr}")
        
        try:
            # Découper en hash, nonce, message
            hash_recu, nonce, msg_recu = data.decode("utf-8").split(":", 2)
            print(f"   Hash reçu : {hash_recu}")
            print(f"   Nonce     : {nonce}")
            print(f"   Message   : {repr(msg_recu)}")
            
            # CORRECTION CRUCIALE : Nettoyer l'encodage du message
            msg_recu = msg_recu.encode("utf-8", errors="replace").decode("utf-8")
            
            # Vérifier si le nonce a déjà été utilisé
            if nonce in used_nonces:
                reponse = " ERREUR - Nonce déjà utilisé (attaque par rejeu !)"
                print("     Attaque par rejeu détectée !")
            else:
                # Recalculer le hash (nonce + message)
                hash_calcule = hashlib.sha256((nonce + msg_recu).encode("utf-8")).hexdigest()
                print(f"   Hash calculé : {hash_calcule}")
                
                # Vérifier l'intégrité
                if hash_recu == hash_calcule:
                    used_nonces.add(nonce)
                    reponse = " INTEGRITE VERIFIEE - Message intact"
                    print("    INTEGRITE OK")
                else:
                    reponse = " ERREUR - Message corrompu !"
                    print("    INTEGRITE KO")
            
            s.sendto(reponse.encode("utf-8"), addr)
            print(f"   ↩️  Réponse envoyée à {addr}\n")
            
        except Exception as e:
            print(f"     Erreur de format : {e}")
            s.sendto(" Format invalide (attendu: hash:nonce:message)".encode("utf-8"), addr)