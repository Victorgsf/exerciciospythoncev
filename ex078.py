num = []

for i in range(0,5):
    num.append(int(input(f"Digite o valor para a posição {i}: ")))

maior = max(num)
menor = min(num)

print(f"O maior valor digitado foi {maior} nas posições ", end="")
for i,v in enumerate(num):
    if v == maior:
        print(f"{i}...", end="")

print()
print(f"O menor valor digitado foi {menor} nas posições ", end="")
for i, v in enumerate(num):
    if v == menor:
        print(f"{i}...", end="")
