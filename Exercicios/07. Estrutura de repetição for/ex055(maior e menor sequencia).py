'''Faça um programa que leia o peso de cinco pessoas, e mostre qual é o maior e menor
peso lidos.'''

print("♣♣MAIOR E MENOR SEQUÊNCIA♣♣")

maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input("Peso da {}ª pessoa: ".format(c)))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print("O maior peso lido foi de {} KG".format(maior))
print("O menor peso lido foi de {} KG".format(menor))
