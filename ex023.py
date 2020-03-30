numaux = ['0', '0', '0', '0']
num = str(input("Digite um numero entre 0 e 9999: "))

for i in range(len(num)):
    numaux[3-i] = num[(len(num)-i-1)]

print("Seu numero tem:")
print("{} milhar".format(numaux[0]))
print("{} centenas".format(numaux[1]))
print("{} dezenas".format(numaux[2]))
print("{} unidades".format(numaux[3]))