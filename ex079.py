num = []

while True:
    valor = int(input("Digite um valor: "))
    if valor in num:
        print("Valor duplicado, não vou adicionar.")
    else:
        num.append(valor)
    continua = " "
    while continua not in "SN":
        continua = str(input("Você deseja continuar? [S/N]")).strip().upper()[0]
    if continua == "N":
        break

num.sort()
print(f"A lista que você digitou foi: {num}")