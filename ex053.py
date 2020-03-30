#OUTRA FORMA DE DETECTAR PALINDROMO

frase = str(input("Digite uma frase: ")).strip().upper()
frase = frase.replace(" ", "")
inverso = ""

for i in range(len(frase)-1, -1, -1):
    inverso += frase[i]

#outro jeito de inverter
#inverso = frase[::-1]

print("{} ao contrário é {}".format(frase, inverso))
if frase == inverso:
    print("Por isso é um palíndromo")
else:
    print("Por isso não é um palíndromo")