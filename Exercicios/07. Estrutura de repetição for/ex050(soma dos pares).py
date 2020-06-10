'''Faça um programa que leia seis números inteiros e mostre a soma apenas daqueles
que forem pares.'''

print("--==SOMA DOS PARES==--")

soma = 0
for c in range(1, 7):
    n = int(input("Digite o {}° número: ".format(c)))
    if n % 2 == 0:
        soma = soma + n
print("A soma de todos os números pares digitados é {}.".format(soma))
print("FIM!!")
