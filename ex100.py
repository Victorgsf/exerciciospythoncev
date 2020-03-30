from random import randint

def sorteia(lst):
    print("Sorteando 5 valores da lista: ", end="")
    for i in range(0, 5):
        lst.append(randint(1, 10))
        print(f"{lst[i]} ", end="")
    print()

def somaPar(lst):
    spar = 0
    for i in lst:
        if i % 2 == 0:
            spar += i
    print(f"Somando os valores pares de {lst}, temos {spar}")


#Programa Principal
lista = []
sorteia(lista)
somaPar(lista)