num = []

for i in range(0,5):
    n = int(input("Digite um valor: "))

    if i == 0 or n > max(num):
        num.append(n)
        print("Adicionado ao final da lista")
    else:
        for c in range(len(num)):
            if n <= num[c]:
                num.insert(c, n)
                print(f"Adicionado na posição {c} da lista...")

print(f"A lista ao final da execução é: {num}")