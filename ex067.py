#cont = 1

'''while True:
    if cont == 1:
        num = int(input("Você deseja ver a tabuada de qual número?"))
        if num < 0:
            break
    print(f"{cont:2} x {num} = {(cont*num)}")
    if cont == 9:
        cont = 0
    cont += 1'''

while True:
    num = int(input("Qual número você deseja ver a tabuada? "))
    if num < 0:
        break

    print("-"*30)
    for i in range(1, 11):
        print(f"{num} x {i:2} = {num*i}")
    print("-" * 30)
