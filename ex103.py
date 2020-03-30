def ficha(nome="<desconhecido>", gols=0):
    print(f"O jogador {nome} fez {gols} no campeonato")


#Programa Principal
n = str(input("Nome: ")).strip()
g = str(input("Número de gols: "))
if g.isnumeric():
    g = int(g)
else:
    g = 0

if n == "":
    ficha(gols=g)
else:
    ficha(n,g)
