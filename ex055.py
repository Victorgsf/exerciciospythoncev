peso = []

for i in range(1, 6):
    peso.append(float(input("Digite o peso da {} pessoa: ".format(i))))

print("A pessoa com mais peso tem {} kg".format(max(peso)))
print("A pessoa com menos peso tem {} kg".format(min(peso)))