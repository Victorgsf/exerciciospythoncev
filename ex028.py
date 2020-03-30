from random import randint
print("- -"*20)
print("Estou pensando em um número...")
print("- -"*20)
pc = randint(0,5)

jog = int(input("Qual número eu pensei? "))

if (pc == jog):
    print("Você ganhou!")
else:
    print("Eu ganhei! Pensei no {}, não no {}".format(pc, jog))