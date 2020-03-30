'''co = float(input("Qual o comprimento do cateto oposto? "))
ca = float(input("Qual o comprimento do cateto adjacente? "))
print("O valor da hipotenusa é {:.2f}".format(((co**2)+(ca**2))**0.5))'''

from math import hypot
co = float(input("Qual o comprimento do cateto oposto? "))
ca = float(input("Qual o comprimento do cateto adjacente? "))
print("O valor da hipotenusa é {:.2f}".format(hypot(co, ca)))