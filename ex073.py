times = ('Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Athletico-PR',
         'São Paulo', 'Internacional', 'Corinthians', 'Fortaleza', 'Goiás',
         'Bahia', 'Vasco', 'Atlético-MG', 'Fluminense', 'Botafogo', 'Ceará',
         'Cruzeiro', 'CSA', 'Chapecoense', 'Avaí')

print("=*"*20)
print("Os 5 primeiros times sao: ", end="")
for i in range(0, 5):
    print(f'{times[i]}, ', end="")

print()
print("=*"*20)
print("Os 4 ultimos times sao: ", end="")
for i in range(16, 20):
    print(f"{times[i]}, ", end="")

print()
print("=*"*20)
print("Os times em ordem alfabetica: ", end="")
print(f"{sorted(times)}")

 
print("=*"*20)
print(f"A Chapecoense esta na {times.index('Chapecoense') + 1} posiçao")