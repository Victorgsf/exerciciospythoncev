mtx = []
somapar = soma3 = maior2 = 0

for lin in range(0, 3):
    mtx.append([])
    for col in range(0, 3):
        mtx[lin].append(int(input(f"Digite um valor para a posição [{lin}] [{col}]: ")))

print("-="*30)
for lin in range(0 ,3):
    for col in range(0,3):
        print(f"[{mtx[lin][col]:^5}]", end="")
        if mtx[lin][col] % 2 == 0:
            somapar += mtx[lin][col]
        if col == 2:
            soma3 += mtx[lin][col]
        if lin == 1:
            if mtx[lin][col] > maior2:
                maior2 = mtx[lin][col]
    print()

print("-="*30)



print(f"A soma de todos os valores pares digitados é {somapar}")
print(f"A soma dos valores da terceira coluna é {soma3}")
print(f"O maior valor da segunda linha é {maior2}")