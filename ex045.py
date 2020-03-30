from random import randint

itens = ["PEDRA", "PAPEL", "TESOURA"]

print(""" Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA""")
jog = int(input("Qual sua opção? "))

pc = randint(0,2)

print("-="*20)
print("Você escolheu {}".format(itens[jog]))
print("O computador escolheu {}".format(itens[pc]))
print("-="*20)

if jog == pc:







