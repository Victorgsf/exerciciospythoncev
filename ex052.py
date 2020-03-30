num = int(input("Digite um número: "))
cont = 0

for i in range(1, num+1):
    if num % i == 0:
        cont += 1

print("O número {} foi divisível {} vezes".format(num, cont))
if cont == 2:
    print("Por isso ele é PRIMO")
else:
    print("por isso ele NÃO É PRIMO")