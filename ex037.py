num = int(input("Digite um número inteiro: "))
print('''Escolha uma das bases para conversão:
[1] Binário
[2] Octal
[3] Hexadecimal''')
opc = int(input("Sua opção: "))

if opc == 1:
    print("{} em binário é {}".format(num, bin(num)))
elif opc == 2:
    print("{} em octal é {}".format(num, oct(num)))
elif opc == 3:
    print("{} em hexadecimal é {}".format(num, hex(num)))
else:
    print("Opção inválida")
