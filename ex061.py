prim = int(input("Qual o primeiro termo? "))
razao = int(input("Qual a razao? "))
pa = prim

i = 1

while i < 11:
    print("{} -> ".format(pa), end="")
    pa += razao
    i += 1