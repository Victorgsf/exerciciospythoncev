from random import randint
numsorteios = int(input("Quantos jogos você quer que eu sorteie? "))
print("-="*5 + f"  SORTEANDO {numsorteios} JOGOS  "+"-="*5)
lista = []

for i in range(0, numsorteios):
    print(f"Jogo {i+1}: ", end="")
    for c in range(0,6):
        n = randint(1, 60)
        while n in lista:
            n = randint(0, 60)
        lista.append(n)
    lista.sort()
    print(lista)
    lista.clear()
