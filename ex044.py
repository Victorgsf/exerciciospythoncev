val = float(input("Qual o valor das compras? R$"))
print("""Qual será a forma de pagamento?
[1] À vista dinheiro/cheque
[2] À vista no cartão
[3] Até 2x no cartão
[4] 3x ou mais no cartão""")
opc = int(input("Qual a sua opção? "))

if opc == 1:
    print("Sua compra terá um desconto e custará R${}".format(val - (val*0.1)))
elif opc == 2:
    print("Sua compra terá um desconto e custará R${}".format(val - (val * 0.05)))
elif opc == 3:
    print("Sua compra sera parecelada em 2x de RS{:.2f} sem juros".format( (val/2)))
elif opc == 4:
    parcela = int(input("Quantas parcelas? "))
    print("Sua compra sera parecelada em {}x de RS{} com juros".format(parcela, ((val + (val*0.2)) / parcela)))
    print("No final ela custará R${}".format(val + (val*0.2)))
else:
    print("Opção inválida")