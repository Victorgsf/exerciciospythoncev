continua = "S"
num = []
cont = 0

while continua == "S":
    num.append(int(input("Digite um numero: ")))
    continua = input("Deseja continuar? [S/N]").strip().upper()[0]
    cont += 1

media = (sum(num)/len(num))

print("Você digitou {} números e a média foi {}".format(cont, media))
print("O maior número foi {} e o menor {}".format(max(num), min(num)))


