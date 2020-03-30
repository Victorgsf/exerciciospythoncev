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


#Programa Principal
n = leiaInt("Digite um número: ")
print(f"Você acabou de digitar o número {n}")