import hashlib

# Message original
msg1 = "Bonjour éàç"
print("Message 1 :", msg1)

# Calcul du hash SHA-256
hash1 = hashlib.sha256(msg1.encode("utf-8")).hexdigest()
print("Hash 1    :", hash1)

# Message légèrement modifié (1 lettre différente !)
msg2 = "BonjouR éàç"  # 'R' majuscule au lieu de 'r'
print("\nMessage 2 :", msg2)

hash2 = hashlib.sha256(msg2.encode("utf-8")).hexdigest()
print("Hash 2    :", hash2)

# Comparaison
print("\n✅ Identiques ?" if hash1 == hash2 else "\n❌ DIFFÉRENTS !")
print(f"   ({sum(c1 != c2 for c1, c2 in zip(hash1, hash2))} caractères différents dans le hash)")