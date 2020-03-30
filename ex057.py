sexo = str(input("Digite o sexo: ")).strip().upper()[0]

while sexo != "M" and sexo != "F":
    sexo = str(input("Digite o sexo: ")).strip().upper()
    if sexo != "M" and sexo != "F":
        print("Dado invalido. Tente novamente")