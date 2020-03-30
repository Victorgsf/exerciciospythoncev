jog = {}

jog["nome"] = str(input("Nome do jogador: ")).strip()
numpartidas = int(input(f"Quantas partidas {jog['nome']} jogou? "))

gols = []
for i in range(0, numpartidas):
    gols.append(int(input(f"    Quantos gols na partida {i+1}? ")))
jog["gols"] = gols[:]

jog["total"] = sum(gols)

print("-="*30)
print(jog)

print("-="*30)
for k, v in jog.items():
    print(f"O campo {k} tem valor {v}")

print("-="*30)
print(f"O jogador {jog['nome']} jogou {numpartidas} partidas")
for i in range(0, numpartidas):
    print(f"    => Na partida {i+1}, fez {jog['gols'][i]} gols")
print(f"Foi um total de {jog['total']} gols.")