from datetime import datetime

trab = {}
trab["nome"] = str(input("Nome: ")).strip()
trab["idade"] = ((datetime.now().year)-(int(input("Data de nascimento: "))))
trab["ctps"] = int(input("Carteira de trabalho: (0 caso não tenha): "))

if trab["ctps"] != 0:
    trab["contratação"] = int(input("Ano de contratação: "))
    trab["salário"] = float(input("Salário: R$"))
    trab["aposentadoria"] = (60 - trab["idade"])

print("-="*30)
for k, v in trab.items():
    print(f"{k} tem o valor {v}")