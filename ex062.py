prim = int(input("Qual o primeiro termo? "))
razao = int(input("Qual a razao? "))
pa = prim
total = 0
mais = 10
i = 1
while mais != 0:
    total += mais
    while i <= total:
        print("{} -> ".format(pa), end="")
        pa += razao
        i += 1
    print("PAUSA")
    mais = int(input("Quantos termos voce quer mostrar a mais? "))
print("Progreçao finalizada com {} termos".format(total))