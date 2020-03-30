dist = float(input("Qual a diastância da  viagem em km? "))

if dist > 200:
    preco = dist * 0.45
else:
    preco = dist * 0.5

print("A viagem custará R$ {:.2f}".format(preco))