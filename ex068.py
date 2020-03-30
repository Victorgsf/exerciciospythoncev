from random import randint

cont = 0

while True:
    jogador = int(input("Digite um numero: "))
    escolha = ' '
    while escolha not in "IP":
        escolha = str(input("Voce quer par ou impar? [P/I]")).strip().upper()[0]

    pc = randint(0,9)

    soma = pc + jogador

    print(f"Voce jogou {jogador} e o computador jogou {pc}. Total de {soma}", end=" ")
    if soma % 2 == 0:       #PAR
        print("DEU PAR")
        if escolha == "P":
            print("VOCE GANHOU")
            cont += 1
        else:
            print("VOCE PERDEU")
            break
    else:
        print("DEU IMPAR")
        if escolha == "I":
            print("VOCE GANHOU")
            cont += 1
        else:
            print("VOCE PERDEU")
            break

print(f"Voce teve um total de {cont} vitorias consecutivas")