pessoas = []
maior = menor = 0

while True:
    dados = []
    dados.append(str(input("Nome: ")).strip())
    dados.append(int(input("Peso: ")))

    if len(pessoas) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        elif dados[1] < menor:
            menor = dados[1]

    pessoas.append(dados[:])
    dados.clear()

    r = " "
    while r not in "SN":
        r = str(input("Você deseja continuar? [S/N] ")).strip().upper()[0]

    if r == "N":
        break

print(f"Foram cadastradas {len(pessoas)} pessoas")


'''for i in range(len(pessoas)):
    if i == 0:
        maior = menor = pessoas[i][1]
    elif pessoas[i][1] > maior:
        maior = pessoas[i][1]
    elif pessoas[i][1] < menor:
        menor = pessoas[i][1]'''
print(f"O maior peso foi de {maior} Kg. Peso de ", end="")

for i in range(len(pessoas)):
    if pessoas[i][1] == maior:
        print(f"[{pessoas[i][0]}] ", end="")

print()
print(f"O menor peso foi de {menor} Kg. Peso de ", end="")
for i in range(len(pessoas)):
    if pessoas[i][1] == menor:
        print(f"[{pessoas[i][0]}] ",  end="")