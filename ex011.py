largura = float(input("Largura da sua parede: "))
altura = float(input("Altura da sua parede: "))
area = largura*altura
print("Sua parede tem dimensão de {}x{} e sua área é de {}m^2".format(largura,altura, (area)))
print("Para pintar essa parede, você precisará de {}l de tinta".format((area/2)))