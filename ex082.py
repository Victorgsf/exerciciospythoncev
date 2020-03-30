list = []

while True:
    list.append(int(input("Digite um valor: ")))

    r = " "
    while r not in "NS":
        r = str(input("Você quer continuar? [S/N] ")).strip().upper()[0]
    if r == "N":
        break

print(f"A lista completa é: {list}")

par = []
impar = []

for i in list:
    if i % 2 == 0:
        par.append(i)
    else:
        impar.append(i)

print(f"A lista de elementos pares é: {par}")
print(f"A lista de elementos ímpares é: {impar}")