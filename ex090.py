dici = {}
dici["nome"] = str(input("Nome: "))
dici["média"] = float(input(f"Média de {dici['nome']}: "))

if dici["média"] >= 7:
    dici["situação"]="Aprovado"
elif 5 <= dici["média"] < 7:
    dici["situação"] = "Recuperação"
else:
    dici["situação"]="Reprovado"

print("-="*30)
for k, v in dici.items():
    print(f"{k} é igual a {v}")
