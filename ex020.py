from random import shuffle
alunos = []
for i in range(4):
    alunos.append(input("Nome do aluno {} ".format(i+1)))
shuffle(alunos)
print("A ordem será: {}".format(alunos))