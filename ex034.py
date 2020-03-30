salario = float(input("Qual o salário? "))

if salario > 1250:
    salario = salario + (salario *0.1)
else:
    salario = salario + (salario * 0.15)

print("O salário passa a ser R$ {:.2f}".format(salario))