num = int(input("Digite um numero para calcular seu fatorial: "))
fat = 1

print("{}! = ".format(num), end="")

while num != 1:
    print("{} x ".format(num), end="")
    fat = fat * num
    num = num - 1

print("1 = {}".format(fat))

