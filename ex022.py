nome = str(input("Qual o seu nome? ")).strip()
print("Seu nome com todas as letras maiusculas: {}".format(nome.upper()))
print("Seu nome com todas as letras minusculas: {}".format(nome.lower()))
numl = 0
nome = nome.split()
for i in range(len(nome)):
    numl += len(nome[i])

print("Seu nome tem {} letras".format(numl))
#Outra maneira
#numl = len(nome)-nome.count(' ')    Importante nao dar o split


print("Seu primeiro nome tem {} letras".format(len(nome[0])))
#Outra maneira
#numlprimeiro = nome.find(' ')    Importante nao dar o split