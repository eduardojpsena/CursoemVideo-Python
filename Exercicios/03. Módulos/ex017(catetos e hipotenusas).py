'''Faça um script que calcule a hipotenusa a partir dos catetos oposto e adjacentes.'''

print(">>>CATETOS E HIPOTENUSA<<<")

import math

cto = float(input("Digite o comprimento do cateto oposto: "))
cta = float(input("Digite o comprimento do cateto adjacente: "))
print("A hipotenusa desse triângulo retangulo vai medir {:.2f}.".format(math.hypot(cto, cta)))
