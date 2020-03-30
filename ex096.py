def area(larg, comp):
    print(f"A área de um terreno de {larg}m x {comp}m é {larg*comp}m2")


#Programa Principal
largura = float(input("Qual a largura do terreno? [m] "))
comprim = float(input("Qual o comprimento do terreno? [m] "))
area(largura, comprim)
