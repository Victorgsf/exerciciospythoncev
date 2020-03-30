menu = 0
valor1 = float(input("Digite o 1 valor: "))
valor2 = float(input("Digite o 2 valor: "))

while menu != 5:
    menu = int(input('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa
    Escolha a opçao:'''))
    print()

    if menu == 1:
        print("A soma de {} e {} e {}".format(valor1, valor2, valor1+valor2))
        print("-="*20)
    elif menu == 2:
        print("A multiplicaçao de {} e {} e {}".format(valor1, valor2, valor1*valor2))
        print("-=" * 20)
    elif menu == 3:
        if valor1 > valor2:
            print("O maior numero entre {} e {} e {}".format(valor1, valor2, valor1))
        elif valor2 > valor1:
            print("O maior numero entre {} e {} e {}".format(valor1, valor2, valor2))
        else:
            print("Os valores sao iguais")
        print("-=" * 20)
    elif menu == 4:
        valor1 = float(input("Digite o 1 valor: "))
        valor2 = float(input("Digite o 2 valor: "))
        print("-=" * 20)
    elif menu > 5:
        print("Opçao invalida. Tente novamente")
        print("-=" * 20)

