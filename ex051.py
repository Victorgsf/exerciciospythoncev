# 10 PRIMEIROS TERMOS PA

prim = int(input("Qual o primeiro termo? "))
razao = int(input("Qual a razão? "))
decimo = prim + (10)*razao

for i in range(prim, decimo, razao):
    print("{} -> ".format(i), end="")
print("ACABOU")