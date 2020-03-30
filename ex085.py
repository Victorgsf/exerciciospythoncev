num = [[],[]]

for i in range(0, 7):
    n = int(input(f"Digite o {i+1} valor: "))

    if n % 2 == 0:
        num[0].append(n)
    else:
        num[1].append(n)

num[0].sort()
num[1].sort()

print(f"Os valores pares são: {num[0]}")
print(f"Os valores ímpares são: {num[1]}")