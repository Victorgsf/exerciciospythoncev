list = []

while True:
    list.append(int(input("Digite um valor: ")))
    r = " "
    while r not in "SsNn":
        r = str(input("Quer continuar? [S/N] ")).strip()[0]
    if r in "Nn":
        break

print(f"Você digitou {len(list)} elementos")
if 5 in list:
    print(f"O número 5 se encontra na lista e sua primeira aparição está no índice {list.index(5)}")
else:
    print("O 5 não se encontra na lista")

list.sort(reverse=True)
print(f"Os valores em ordem decrescente são: {list}")