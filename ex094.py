pessoa = {}
todos = []

while True:
    #Pegando Dados
    pessoa["nome"] = str(input("Nome: ")).strip()
    while True:
        pessoa["sexo"] = str(input("Sexo: [M/F] ")).strip().upper()[0]
        if pessoa["sexo"] in "MF":
            break
        else:
            print("Responda M ou F")
    pessoa["idade"] = int(input("Idade: "))

    #Guardando na lista
    todos.append(pessoa.copy())
    pessoa.clear()

    #Continuar?
    while True:
        r = str(input("Você deseja continuar? [S/N] ")).strip().upper()[0]
        if r in "SN":
            break
        else:
            print("Responda com S ou N")
    if r == "N":
        break

print("-="*30)
print(f"A) Ao todo temos {len(todos)} pessoas cadastradas")

#Média de idade
media = 0
for i in range(len(todos)):
    media += todos[i]["idade"]
media = media/len(todos)
print(f"B) A média de idade foi de {media:}")

print("C) Lista de pessoas que estão com idade acima da média:")
for i in range(len(todos)):
    if todos[i]["idade"] > media:
        for k, v in todos[i].items():
            print(f"    {k} = {v}; ", end="")
        print()