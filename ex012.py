preco = float(input("Qual o preço do seu produto? R$"))
print("O produto que cutava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}".format(preco, (preco-(preco*0.05))))