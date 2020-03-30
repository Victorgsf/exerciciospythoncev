expr = str(input("Digite a expressão: "))
abre = fecha = 0

for i in range(len(expr)):
    if expr[i] == "(":
        abre += 1
    elif expr[i] == ")":
        fecha += 1

if abre == fecha:
    print("A expressão é válida")
else:
    print(("A expressão não é válida"))