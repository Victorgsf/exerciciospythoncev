from datetime import date
atual = date.today().year
nasc = int(input("Qual o ano do seu naascimento? "))
idade = atual - nasc

print("Quem nasceu em {} tem {} em {}".format(nasc, idade, atual))
if idade > 18:
    print("Você já deveria ter se alistado há {} anos".format(idade-18))
    print("Seu alistamento foi em {}".format(atual - (idade-18)))
elif idade < 18:
    print("Você irá se alistar em {} anos".format(18 - idade))
    print("Seu alistamento será em {}".format(atual + (18 - idade)))
else:
    print("Você deverá se alistar esse ano!")