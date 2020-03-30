palavras = ('viajar', 'elegante', 'animal', 'carro', 'brasileiro', 'abacate')
vogais = "aeiou"

for palavra in palavras:
    print(f"A palavra {palavra} tem as vogais: ", end="")
    for letra in palavra:
        if letra.lower() in vogais:
            print(f"{letra} ", end="")
    print()
