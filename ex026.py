frase = str(input("Digite uma frase: ")).strip()
frase = frase.lower()

numa = frase.count("a")
print("A letra 'A' aparece {} vezes".format(numa))

print("A posiçao do primeiro 'A' e {}".format(frase.find("a")+1))
print("A posiçao do primeiro 'A' e {}".format(frase.rfind("a")+1))
