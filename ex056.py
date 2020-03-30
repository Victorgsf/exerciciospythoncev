nome = []
idade = []
sexo = []
velho = 0
qntnova = 0

for i in range(4):
    print("{} pessoa:".format(i+1))
    nome.append( str(input("Nome: ")).strip())
    idade.append( int(input("Idade: ")) )
    sexo.append( str(input("Sexo [M/F]:")).strip().upper())

    if sexo[i] == "M":
        if idade[i] > velho:
            velho = idade[i]
            posvelho = i
    if sexo[i] == "F":
        if idade[i] < 20:
            qntnova += 1


media = sum(idade)/len(idade)
print("A media de idade do grupo e de {} anos".format(media))

print("O homem mais velho tem {} anos e se chama {}".format(velho, nome[posvelho]))

print("Ha {} mulheres com menos de 20 anos".format(qntnova))