vel = float(input("Qual sua velocidade? "))

if vel <= 80:
    print("Tenha um bom dia")
else:
    print("Você excedeu o limete de 80km/h")
    multa = (vel - 80)*7
    print("Sua multa será de R$ {:.2f}".format(multa))