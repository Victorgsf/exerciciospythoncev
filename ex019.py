import random
alunos = []

for i in range(4):
    alunos.append(input("Qual o nome do aluno {}? ".format(i+1)))

'''sort = random.randint(0,3)
print("O aluno sorteado foi {}".format(alunos[sort]))'''

print("O aluno sorteado foi {}".format(random.choice(alunos)))