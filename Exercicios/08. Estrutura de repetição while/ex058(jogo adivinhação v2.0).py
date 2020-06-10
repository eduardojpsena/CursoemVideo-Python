'''Faça um jogo da adivinhação com while, número de 1 a 10, o jogo se repete até o
jogador acertar e no final mostrar quantos palpites do jogador deu.'''

print("=-=-JOGO DA ADIVINHAÇÃO-=-=")

import random
computer = random.randint(1, 10)
player = int(input("Digite um número entre 1 e 10: "))
c = 0
while computer != player:
    print("Errou, Você jogou {} e o computador jogou {}.".format(player, computer))
    player = int(input("Tente novamente: "))
    computer = random.randint(1, 10)
    c += 1
print("Parabéns você acertou."
      " \nNúmeros de palpites errados: {}".format(c))
