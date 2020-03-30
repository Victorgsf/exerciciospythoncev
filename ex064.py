soma = cont = num =  0

while num != 999:
    num = int(input("Digite um numero: "))
    if num != 999:
        soma += num
        cont += 1

print("Voce digitou {} numeros e a soma deles e {}".format(cont, soma))