from ex112.utilidadescev import moeda
from ex112.utilidadescev.dado import leiaDinheiro

preco = leiaDinheiro("Digite o preço: R$")
moeda.resumo(preco, 10, 10)