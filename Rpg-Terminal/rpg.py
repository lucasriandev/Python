import random

print("=" * 40)
print("⚔️ AVENTURA NA FLORESTA SOMBRIA ⚔️")
print("=" * 40)

nome = input("Digite o nome do seu herói: ")

hp = 100
pocao = 3

print(f"\nBem-vindo, {nome}!")
print("Seu objetivo é encontrar o Cristal da Floresta.")

while True:

    if hp <= 0:
        print("\nVocê caiu em batalha...")
        print("GAME OVER!")
        break

    print("\n----------------------------")
    print(f"Vida: {hp}")
    print(f"Poções: {pocao}")
    print("----------------------------")

    print("\nEscolha um caminho:")
    print("1 - Entrar na caverna")
    print("2 - Seguir pela floresta")
    print("3 - Descansar")
    print("4 - Desistir")

    escolha = input("Opção: ")

    if escolha == "1":

        print("\nVocê entrou na caverna!")

        if random.randint(1, 100) <= 60:
            inimigo_hp = 40
            print("Um Goblin apareceu!")

            while inimigo_hp > 0 and hp > 0:

                print(f"\nSua vida: {hp}")
                print(f"Vida do Goblin: {inimigo_hp}")

                print("1 - Atacar")
                print("2 - Defender")
                print("3 - Usar poção")

                acao = input("Escolha: ")

                if acao == "1":
                    dano = random.randint(10, 20)
                    inimigo_hp -= dano
                    print(f"Você causou {dano} de dano!")

                elif acao == "2":
                    print("Você se preparou para defender.")

                elif acao == "3":
                    if pocao > 0:
                        cura = random.randint(20, 35)
                        hp += cura
                        if hp > 100:
                            hp = 100
                        pocao -= 1
                        print(f"Você recuperou {cura} de vida!")
                    else:
                        print("Você não possui poções!")

                else:
                    print("Opção inválida.")
                    continue

                if inimigo_hp > 0:
                    dano_inimigo = random.randint(8, 18)

                    if acao == "2":
                        dano_inimigo //= 2

                    hp -= dano_inimigo
                    print(f"O Goblin atacou causando {dano_inimigo} de dano!")

            if hp > 0:
                print("\nVocê derrotou o Goblin!")

        else:
            print("A caverna estava vazia. Você encontrou uma poção!")
            pocao += 1

    elif escolha == "2":

        print("\nVocê caminhou pela floresta...")

        evento = random.randint(1, 3)

        if evento == 1:
            print("Você encontrou frutas e recuperou 15 de vida.")
            hp += 15
            if hp > 100:
                hp = 100

        elif evento == 2:
            print("Você encontrou uma poção.")
            pocao += 1

        else:
            print("Você encontrou o Cristal da Floresta!")
            print("\nPARABÉNS!")
            print(f"{nome} completou a aventura!")
            break

    elif escolha == "3":

        print("\nVocê descansou.")
        hp += 10

        if hp > 100:
            hp = 100

        print("Você recuperou 10 de vida.")

    elif escolha == "4":

        print("\nVocê decidiu voltar para casa.")
        print("Fim da aventura.")
        break

    else:
        print("Escolha inválida.")