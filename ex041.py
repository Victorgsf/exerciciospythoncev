from datetime import date
atual = date.today().year
nasc = int(input("Qual ano você nasceu? "))
idade = atual - nasc

if idade <= 9:
    print("MIRIM")
elif 9 < idade <= 14:
    print("INFANTIL")
elif 14 < idade <= 25:
    print("SENIOR")
else:
    print("MASTER")