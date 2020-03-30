tot = maismil = cont = menor =  0
barato = " "

while True:
    produto = str(input("Qual o nome do produto? ")).strip()
    valor = float(input("Preço: R$"))
    quebra = " "
    while quebra not in "SN":
        quebra = str(input("Voce deseja continuar? [S/N]")).strip().upper()[0]
    cont += 1

    tot += valor

    if valor > 1000:
        maismil += 1

    if cont == 1:
        menor = valor
        barato = produto
    else:
        if valor < menor:
            menor = valor
            barato = produto


    if quebra == "N":
        break

print(f"O total da compra foi {tot}")
print(f"Ha {maismil} custando mais de mil reais")
print(f"O produto mais barato custou R${menor:.2f} e eh o {barato}")