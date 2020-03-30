def aumentar(val=0, porc=0):
    val += val*(porc/100)
    return val


def diminuir(val=0, porc):
    val -= val*(porc/100)
    return val


def dobro(val=0):
    val = 2*val
    return val


def metade(val=0):
    val = val/2
    return val

def moeda(val=0, moeda="R$"):
    return f"{moeda}{val:.2f}".replace(".", ",")
