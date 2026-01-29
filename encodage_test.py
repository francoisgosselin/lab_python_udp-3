from pathlib import Path

p = Path("data/message.txt")

# Lecture en mode TEXTE (comme un humain)
s = p.read_text(encoding="utf-8")
print("=== MODE TEXTE ===")
print("Type :", type(s))
print("Longueur (caractères) :", len(s))
print("Contenu :", repr(s))

# Lecture en mode BINAIRE (comme l'ordinateur)
b = p.read_bytes()
print("\n=== MODE BINAIRE ===")
print("Type :", type(b))
print("Longueur (octets) :", len(b))
print("Contenu (hex) :", b.hex()[:40] + "...")

# Conversion texte → octets
b2 = s.encode("utf-8")
print("\n=== CONVERSION ===")
print("Texte → octets :", len(s), "caractères →", len(b2), "octets")
print("Identiques ?", b == b2)