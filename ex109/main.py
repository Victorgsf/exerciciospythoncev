from ex109 import moeda

preco = float(input("Digite o preço: R$"))
print(f"A metade de {moeda.moeda(preco)} é {moeda.metade(preco)}")
print(f"O dobro de {moeda.moeda(preco)} é {moeda.dobro(preco)}")
print(f"Aumentando 10% de {moeda.moeda(preco)} ficamos com {moeda.aumentar(preco, 10)}")
