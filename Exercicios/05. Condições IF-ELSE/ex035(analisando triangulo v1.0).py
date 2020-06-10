'''Faça um programa que leia o comprimento de 3 segmentos de retas e informe se elas
podem formar um triângulo.'''

print(">>>ANÁLISANDO TRIÂNGULO<<<")

r1 = float(input("Digite o comprimento da primeira reta: "))
r2 = float(input("Digite o comprimento da segunda reta: "))
r3 = float(input("Digite o comprimento da terceira reta: "))

if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print("É possivel formar um triângulo com esses segmentos de retas!")
else:
    print("Não é possivel formar um triângulo com esses segmentos de retas!")
