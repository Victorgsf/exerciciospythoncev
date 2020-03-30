casa = float(input("Qual o valor da casa? "))
sal = float(input("Qual o salário do comprador? "))
anos = float(input("Em quantos anos será pago? "))

if ((casa/(anos*12)) > (sal*0.3)):
    print("Imprestimo Negado")
else:
    print("Empréstimo Concedido")