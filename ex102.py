def fatorial(n, show=False):
    '''
        -> Calcula o fatorial do número passado
    :param n: Número a ser calculado o fatorial
    :param show: (opc) Mostrar ou não a conta feita
    :return: O valor do fatorial de n
    '''

    cont = n
    fat = 1
    while cont >= 1:
        fat *= cont
        if show == True:
            if cont == 1:
                print(f"{cont} = ", end="")
            else:
                print(f"{cont} x ", end="")
        cont -= 1
    return fat


#print(fatorial(5))
help(fatorial)
