def leiaInt(msg):
    """
        ->Função que faz a validação do input de um inteiro
    :param msg: Mensagem
    :return: Número inteiro digitado
    Feito por Victor Gabriel
    """
    while True:
        try:
            num = int(input(msg))
        except:
            print("ERRO! Digite um número inteiro.")
        else:
            return num


def leiaFloat(msg):
    while True:
        try:
            num = str(input(msg)).strip().replace(",", ".")
            num = float(num)
        except:
            print("Digite um número decimal válido")
        else:
            return num


#Programa Principal
n = leiaInt("Digite um número inteiro: ")
print(f"Você acabou de digitar o número {n}")

f = leiaFloat("Digite um número float: ")
print(f"Você acabou de digitar o número {f}")