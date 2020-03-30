def notas(*n, sit=False):
    """
        -> Função que analisa notas e situações de alunos.
    :param n: Notas do aluno
    :param sit: (opcional) Se == True traz a situação do aluno de acordo com sua média
    :return: Dicionário com os campos total(número de notas), maior, menor (notas), média, e situação
    Feito por Victor Gabriel
    """
    dicnotas = {}
    dicnotas["total"] = len(n)
    dicnotas["maior"] = max(n)
    dicnotas["menor"] = min(n)
    dicnotas["média"] = sum(n)/dicnotas["total"]
    if sit:
        if dicnotas["média"] >= 7:
            dicnotas["situação"] = "BOA"
        elif dicnotas["média"] < 6:
            dicnotas["situação"] = "RUIM"
        else:
            dicnotas["situação"] = "RAZOÁVEL"

    return dicnotas



#Programa Principal
resp = notas(10, 2.5, 7, 10)
print(resp)
help(notas)