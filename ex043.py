peso = float(input("Qual o seu peso em kg? "))
alt = float(input("Qual a sua altura em m? "))

imc = peso/(alt**2)

if imc < 18.5:
    print("ABAIXO DO PESO")
elif 18.5 <= imc < 25:
    print("PESO NORMAL")
elif 25 <= imc < 30:
    print("SOBREPESO")
elif 30 <= imc < 40:
    print("OBESIDADE")
else:
    print("OBESIDADE MORBIDA")