numtup = ("zero", "um", "dois", "tres", "quatro", "cinco",
          "seis","sete", "oito", "nove", "dez", "onze", "doze",
          "treze", "quatorze", "quinze", "dezesseis", "dezesete",
          "dezoito", "dezenove", "vinte" )
while True:
    num  = 21
    while num > 20 or num < 0:
        num = int(input("Digite um numero entre 0 e 20: "))

    print(f"Voce digitou {numtup[num]}")

    continua = " "
    while continua not in "SN":
        continua  = str(input("Voce quer continuar? [S/N]")).upper().strip()[0]
    if continua == "N":
        break
