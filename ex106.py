cor = {"semcor":"\033[m", "vermelho":"\033[0;30;41m", "verde":"\033[0;30;42m",
       "amarelo":"\033[0;30;43m", "azul":"\033[0;30;44m", "roxo":"\033[0;30;45m", "branco":"\033[7;30m"
       }


def ajuda(com):
    global cor
    print(cor["branco"], end="")
    help(com)
    print(cor["semcor"], end="")

def titulo(msg, c="semcor"):
    global cor
    tam = len(msg) + 4
    print(cor[c], end="")
    print("~"*tam)
    print(f"  {msg}")
    print("~"*tam)
    print(cor["semcor"], end="")


#Programa Principal
comando = " "

while True:
    titulo("SISTEMA DE AJUDA PyHELP", "verde")
    comando = str(input(cor["azul"]+"Função ou biblioteca > "+cor["semcor"])).strip()
    if comando.upper() == "FIM":
        break
    else:
        ajuda(comando)