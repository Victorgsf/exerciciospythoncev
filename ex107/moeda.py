def aumentar(val, porc):
    val += val*(porc/100)
    return val


def diminuir(val, porc):
    val -= val*(porc/100)
    return val


def dobro(val):
    val = 2*val
    return val


def metade(val):
    val = val/2
    return val