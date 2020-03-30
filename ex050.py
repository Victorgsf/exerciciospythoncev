soma = 0
for i in range(0,6):
    num = int(input("Digite o valor: "))
    if num % 2 == 0:
        soma += num

print("A soma dos valores pares digitados é {}".format(soma))