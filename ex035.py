retas =[]
for i in range(3):
    retas.append(float(input("Qual o tamanho do segmento de reta {}: ".format(i+1))))

retas = sorted(retas)

if retas[2] >= (retas[0]+retas[1]):
    print("Essas retas não podem formar um triângulo")
else:
    print("Essas retas podem formar um triângulo")
