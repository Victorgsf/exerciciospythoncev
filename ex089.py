list = []
dados = []

while True:
    dados.append(str(input("Nome: ")).strip())
    dados.append(float(input("Nota 1: ")))
    dados.append(float(input("Nota 2: ")))

    list.append(dados[:])
    dados.clear()

    r = " "
    while r not in "SN":
        r = str(input("Você deseja continuar? [S/N] ")).strip().upper()[0]

    if r == "N":
        break

print("-=" * 30)
print(f"{'No.':<4}{'NOME':<10}{'MÉDIA':<5}")
print("-"*25)
for i in range(len(list)):
    print(f"{i:<4}{list[i][0]:<10}{(list[i][1] + list[i][2])/2:<5.2f}")
print("-"*25)

while True:
    print("-" * 100)
    indice = int(input(f"Digite o número do aluno o qual você deseja ver as notas. (999 para sair)"))
    if indice < len(list):
        print(f"Notas de {list[indice][0]} são: [{list[indice][1]} {list[indice][2]}]")
    elif indice == 999:
        break
    else:
        print("Digite um número válido")