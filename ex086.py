mtx = [[], [], []]

for lin in range(0,3):
    for col in range(0,3):
        mtx[lin].append(int(input(f"Digite o valor para a posição [{lin}] [{col}]: ")))

print("-="*30)

for lin in range(0,3):
    for col in range(0,3):
        print(f"[{mtx[lin][col]:^4}] ", end="")
    print()