'''Calcular a quantidade de tinta necessaria para pintar uma parede.'''

print(">>>> PINTURA DE PAREDE <<<<")

larg = float(input("Digite a largura da parede em metros: "))
alt = float(input("Digite a altura da parede em metros: "))
area = larg*alt
tinta = area / 2
print("→ É necessário {} litros de tinta para pintar {} m² de parede!".format(tinta, area))
