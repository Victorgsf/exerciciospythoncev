#SOMA DOS NUMEROS IMPARES DIVISIVEIS POR TRES NO INTERVALO DE 1 A 500

soma = 0
cont = 0
for i in range(3, 501, 3):
    if i % 2 != 0:
        cont += 1
        soma += i

print("A soma dos {} valores encontrados é {}".format(cont, soma))