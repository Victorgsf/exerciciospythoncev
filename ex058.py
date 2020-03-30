from random import randint

pc = randint(0,10)
print("Acabei de pensar em um numero entre 0 e 10")

jog = int(input("Qual seu palpite? "))
tentativa = 1

while jog != pc:
    if jog > pc:
        print("Menos... Tente mais uma vez")
    else:
        print("Mais... Tente mais uma vez")
    jog = int(input("Qual seu palpite? "))
    tentativa += 1

print("Acertou com {} tentativas. Parabens.".format(tentativa))