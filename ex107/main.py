from ex107 import moeda

preco = float(input("Digite o preço: R$"))
print(f"A metade de R${preco} é R${moeda.metade(preco)}")
print(f"O dobro de R${preco} é R${moeda.dobro(preco)}")
print(f"Aumentando 10% de R${preco} ficamos com R${moeda.aumentar(preco, 10)}")
