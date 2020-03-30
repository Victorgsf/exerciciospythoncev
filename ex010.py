cotacao = float(input("Cotação dólar: R$ "))
carteira = float(input("Quantos reais vc tem? R$ "))
print("Você pode comprar: US$ {:.2f}".format((carteira/cotacao)))
