nome = str(input("Qual o seu nome? ")).strip().split()
len = len(nome)
print("Seu primeiro nome e: {}".format(nome[0]))
print("Seu ultimo nome e: {}".format(nome[len-1]))