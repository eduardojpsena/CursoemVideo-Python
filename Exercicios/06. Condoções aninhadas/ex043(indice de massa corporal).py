'''Faça um programa que leia altura e peso para calcular o IMC de uma pessoa e
mostre: Abaixo do peso para IMC menor que 18.5, Peso ideal com IMC entre 18.5 e 25,
Sobrepeso 26 a 30, Obesidade 31 a 40, acima de 40 Obesidade móbida.'''

print(">>>INDICE DE MASSA CORPORAL<<<")

peso = float(input("Peso (Kg): "))
altura = float(input("Altura (m): "))
imc = peso / (altura ** 2)

if imc < 18.5:
    print("ABAIXO DO PESO!")
elif 18.5 <= imc <= 25:
    print(("PESO IDEAL!"))
elif 25 < imc <= 30:
    print("ACIMA DO PESO!")
elif 30 < imc <= 40:
    print("OBESIDADE!")
else:
    print("OBESIDADE MÓRBIDA!")
