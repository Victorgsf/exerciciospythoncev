def leiaDinheiro(msg):
    while True:
        num = str(input(msg)).strip().replace(",", ".")
        if num.isalpha() or num.isalnum() or num == "":
            print("Digite um valor válido.")
        else:
            num = float(num)
            break

    return num


def leiaInt(msg):
    """
        ->Função que faz a validação do input de um inteiro
    :param msg: Mensagem
    :return: Número inteiro digitado
    Feito por Victor Gabriel
    """
    while True:
        num = str(input(msg)).strip()
        if num.isnumeric():
            break
        else:
            print("ERRO! Digite um número inteiro.")
    return int(num)
