'''Faça um programa que jogue PAR ou IMPAR com o computador. O jogo será encerrado
quando o jogador perder, mostrando o total de vitórias consecultivas'''

print("~~~~PAR OU IMPAR~~~~")

from random import randint

c = 0
while True:
    computer = randint(0, 11)
    player = int(input("Selecione um valor: "))
    soma = computer + player
    selection = ' '
    while selection not in 'PI':
        selection = str(input("PAR ou ÍMPAR? [P/I]: ")).strip().upper()[0]
    print(f"Você jogou {player} e computador {computer}. Total de {soma}.", end=' ')
    if selection in 'P':
        if soma % 2 == 0:
            print("Deu PAR! \nVocê Ganhou.")
            c += 1
        else:
            print("Deu ÍMPAR!.")
            break
    elif selection in 'I':
        if soma % 2 == 1:
            print("Deu ÍMPAR! \nVocê Ganhou.")
            c += 1
        else:
            print("Deu ÍMPAR!")
            break
print(f"GAME OVER! Você venceu {c} vezes.")
