jog = {}
time = []

while True:
    jog["nome"] = str(input("Nome do jogador: ")).strip()
    numpartidas = int(input(f"Quantas partidas {jog['nome']} jogou? "))

    gols = []
    for i in range(0, numpartidas):
        gols.append(int(input(f"    Quantos gols na partida {i+1}? ")))
    jog["gols"] = gols[:]

    jog["total"] = sum(gols)

    time.append(jog.copy())
    jog.clear()

    while True:
        r = str(input("Você deseja continuar? [S/N] ")).strip().upper()[0]
        if r in "SN":
            break
        else:
            print("Responda com S ouu N")
    if r == "N":
        break
print(time[0]['nome'])
print(time[0]['gols'])
print(time[0]['total'])
print("-="*30)

#Tabela
print(f"{'cod':<4}{'Nome':<10}{'gols':<10}{'total':<5}")
print("-"*25)
for i in range(len(time)):
    print(f"{i:<4} {time[i]['nome']:<7} {str(time[i]['gols']):<7} {time[i]['total']:<5}")
print("-" * 25)

print("-="*30)

while True:
    print("-" * 100)
    indice = int(input(f"Mostrar dados de qual jogador?. (999 para sair)"))
    if indice < len(time):
       print(f"----- LEVANTAMENTO DO JOGADOR {time[indice]['nome']}")
       for i, v in enumerate(time[indice]['gols']):
           print(f"Na partida {i+1} fez {v} gols")
    elif indice == 999:
        break
    else:
        print("Digite um número válido")