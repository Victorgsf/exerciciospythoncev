dias = int(input("Quantos dias alugados? "))
km = float(input("Qual a distância percorrida em km? "))
total = float( (dias * 60) + (km * 0.15) )
print("O valor a ser pago deve ser R$ {:.2f}".format(total))