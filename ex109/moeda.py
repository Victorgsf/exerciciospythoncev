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
