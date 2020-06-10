'''Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e também indique o maior e o menor
valor que estão na tupla.'''

print("~~~MAIOR E MENOR VALOR EM TUPLA~~~")

import random

numalt = (random.randint(0, 9), random.randint(0, 9), random.randint(0, 9),
          random.randint(0, 9), random.randint(0, 9))
print("Os valores sorteados foram:", end=' ')
for n in numalt:
    print("{}".format(n), end=' ')
print("\nO maior valor sorteado foi: {}".format(max(numalt)))
print("O menor valor sorteado foi: {}".format(min(numalt)))
