num = []
for i in range(3):
    num.append(float(input("Digite um número: ")))

num = sorted(num)
print("O menor número é: {}".format(num[0]))
print("O maior número é: {}".format(num[2]))