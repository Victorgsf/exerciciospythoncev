import math
ang = float(input("Digite o angulo em graus: "))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))
print("O sin é {:.2f}".format(sen))
print("O cos é {:.2f}".format(cos))
print("A tan é {:.2f}".format(tan))