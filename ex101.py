def voto(nasc):
    '''
        -> Função que diz se o voto é NEGADO, FACULTATIVO ou OBRIGATÓRIO de acordo com o ano de nascimento
    :param ano: Ano de Nascimento
    :return: Situação do voto
    Criado por Victor Gabriel
    '''
    from datetime import datetime
    global idade
    idade = datetime.now().year - nasc

    if 18 <= idade <= 70:
        return "OBRIGATÓRIO"
    elif idade < 16:
        return "NEGADO"
    else :
        return "FACULTATIVO"


#Programa Principal
idade = 0
v = voto(int(input("Qual sua data de nascimento? ")))
print(f"Com {idade} anos o voto é {v}")