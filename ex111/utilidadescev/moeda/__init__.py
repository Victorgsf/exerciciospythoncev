def aumentar(val=0, porc=0, formatar=True):
    val += val*(porc/100)
    if formatar:
        val = moeda(val)

    return val


def diminuir(val=0, porc=0, formatar=True):
    val -= val*(porc/100)
    if formatar:
        val = moeda(val)

    return val


def dobro(val=0, formatar=True):
    val = 2*val
    if formatar:
        val = moeda(val)

    return val


def metade(val=0, formatar=True):
    val = val/2
    if formatar:
        val = moeda(val)

    return val

def moeda(val=0, moeda="R$"):
    return f"{moeda}{val:.2f}".replace(".", ",")

def resumo(val=0, aumen=0, dim=0):
    print("-" * 40)
    print(f"{'RESUMO DO VALOR':^40}")
    print("-" * 40)
    print(f"{'Preço analisado:':<20}{moeda(val):<20}")
    print(f"{'Dobro do preço:':<20}{dobro(val):<20}")
    print(f"{'Metade do preço:':<20}{metade(val):<20}")
    print(f"{aumen:2}{'% de aumento:':<18}{aumentar(val, aumen):<20}")
    print(f"{dim:2}{'% de redução:':<18}{diminuir(val, dim):<20}")
    print("-" * 40)


