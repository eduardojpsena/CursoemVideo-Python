'''Crie um programa que faça o computador pensar em um numero inteiro entre 0 e 5 e
peça para o usuário tentar descobrir qual foi o numero escolhido pelo computador.'''

print(">>>JOGO DA ADIVIHAÇÃO<<<")

import random
import time

print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-")
print("Tente adivinhar o número de 0 a 5 que pensei...")
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-")
computador = random.randint(0, 5)
player = int(input("Em que número pensei? "))
if computador == player:
    print("PROCESSANDO...")
    time.sleep(2)
    print("Parabens você acertou.")
else:
    print("PROCESSANDO...")
    time.sleep(2)
    print("Que pena, não foi dessa vez. O número que pensei foi {}.".format(computador))
