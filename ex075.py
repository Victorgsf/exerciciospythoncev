num = (int(input("Digite um valor: ")),int(input("Digite um valor: ")), int(input("Digite um valor: ")), int(input("Digite um valor: ")))

print(f"O numero 9 apareceu {num.count(9)} vezes")
if 3 in num:
    print(f"O numero 3 aparece primeiro na posiçao {num.index(3)+1}")
else:
    print("O numero 3 nao esta presente")

print("Os numeros pares sao: ", end="")
for i in num:
    if i % 2 == 0:
        print(f"{i} ", end="")
