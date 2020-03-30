def contador(ini, fim, passo):
    print("-="*30)
    print(f"Contagem de {ini} até {fim} de {passo} em {passo}")
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    if ini <= fim:
        for i in range(ini, fim+1, passo):
            print(f"{i} ", end="")
        print("FIM!")
    else:
        for i in range(ini, fim-1, -passo):
            print(f"{i} ", end="")
        print("FIM!")


#Programa Principal
contador(1, 10, 1)
contador(10, 0, 2)
print("-="*30)
print("Personalize a contagem")
i = int(input("Início: "))
f = int(input("Fim: "))
p = int(input("Passo: "))
contador(i, f, p)