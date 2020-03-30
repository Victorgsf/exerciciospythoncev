from random import randint
from operator import itemgetter

jogadores = {"jogador1":0, "jogador2":0, "jogador3":0, "jogador4":0 }

for k in jogadores.keys():
    jogadores[k] = randint(1,6)

for k, v in jogadores.items():
    print(f"{k} tirou {v}")

print("-="*30)
print("====    RANKING    ====")


pos = jogadores.values()
pos = sorted(pos)

jog = {}

for i in range(0,4):
    for k in jogadores.keys():
        if jogadores[k] == pos[i]:
            jog[k] = jogadores[k]

cont = 1
for k, v in jog.items():
    print(f"{cont} lugar: {k} com {v}")
    cont += 1

#Outro método
'''jog = sorted(jogadores.items(), key=itemgetter(1), reverse=True)

for i, v in enumerate(jog):
    print(f"{i+1} lugar: {v[0]} com {v[1]}")'''