maiores = homens = mulherm20 = 0

while True:
    idade = int(input("Idade: "))
    sexo = " "
    while sexo not in "MF":
        sexo = str(input("Sexo [M/F]: ")).strip().upper()[0]

    quebra = " "
    while quebra not in "SN":
        quebra = str(input("Deseja continuar? [S/N]")).strip().upper()[0]

    if idade > 18:
        maiores += 1
    if sexo == "M":
        homens += 1
    if sexo == "F" and idade < 20:
        mulherm20 += 1

    if quebra == "N":
        break

print(f"Total de pessoas com mais de 18 anos: {maiores}")
print(f"Total de homens cadastrados: {homens}")
print(f"Total de mulheres com menos de 20 anos: {mulherm20}")