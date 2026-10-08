import random

# Lista com os 8 estilos de batalha disponíveis na roleta
personagens = [
    "Star and Stripe (Original)",
    "Lady Nagant (Original)",
    "Gentle Criminal (Original)",
    "Izuku Midoriya (Full Bullet)",
    "Eijiro Kirishima (Red Drive)",
    "All Might (Gatling)",
    "Tomura Shigaraki (Thousand-Hand Break)",
    "Overhaul (Blighted Precipice)"
]

def girar_roleta():
    return random.choice(personagens)

print("--- Simulando 1x Roll ---")
print(f"Personagem obtido: {girar_roleta()}\n")

print("--- Simulando 10x Roll ---")
for i in range(1, 11):
    print(f"Giro {i}: {girar_roleta()}")