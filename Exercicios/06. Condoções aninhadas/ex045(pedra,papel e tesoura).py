'''Faça um jogo de Jokenpô.'''

print("\033[0;33m-=-=-JO KEN PÔ-=-=-\033[m")

from emoji import emojize
from random import randint
from time import sleep

pedra = emojize(":fist:", use_aliases=True)
papel = emojize(":raised_hand:", use_aliases=True)
tesoura = emojize(":v:", use_aliases=True)
itens = (pedra, papel, tesoura)

player = int(input('''Suas opções:
• [0] PEDRA
• [1] PAPEL
• [2] TESOURA
\033[0;33mQual é a sua escolha?\033[m '''))
computer = randint(0, 2)

print("JO", pedra)
sleep(1)
print("KEN", papel)
sleep(1)
print("PO", tesoura)
sleep(1)

print("\033[0;33m=-\033[m" * 12)
print("\033[0;35mVocê jogou {}\033[m".format(itens[player]))
print("\033[0;31mO computador jogou {}\033[m".format(itens[computer]))
print("\033[0;33m=-\033[m" * 12)

if computer == player:
    print("EMPATE!!")
elif computer == 0 and player == 2 or computer == 1 and player == 0 or computer == 2 and player == 1:
    print("VOCÊ PERDEU!!")
elif player == 0 and computer == 2 or player == 1 and computer == 0 or player == 2 and computer == 1:
    print("VOCÊ GANHOU!!")
else:
    print("Opção invalida, tente novamente!")
