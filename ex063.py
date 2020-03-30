print("-"*30)
print("Sequencia de Fibonacci")
print("-"*30)

termos = int(input("Quantos termos voce quer mostrar? "))
i = 0
fibo = []

while i < termos:
    if i == 0:
        fibo.append(0)
    elif i == 1:
        fibo.append(1)
    else:
        fibo.append(fibo[i-1]+fibo[i-2])
    print("{} -> ".format(fibo[i]), end="")
    i += 1
print("FIM")