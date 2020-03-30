notas = []

for i in range(2):
    notas.append(float(input("Digite a nota {}: ".format(i+1))))

media = sum(notas)/len(notas)

if media < 5:
    print("Reprovado")
elif media >= 5 and media <= 6.9:
    print("Recuperação")
else:
    print("Aprovado")