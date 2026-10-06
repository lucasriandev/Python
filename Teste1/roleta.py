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
    # A função choice() escolhe um item com peso igual para todos
    return random.choice(personagens)

# Testando 1 giro
print("--- Simulando 1x Roll ---")
print(f"Personagem obtido: {girar_roleta()}\n")

# Testando 10 giros seguidos (como no botão "10x Roll" do jogo)
print("--- Simulando 10x Roll ---")
for i in range(1, 11):
    print(f"Giro {i}: {girar_roleta()}")