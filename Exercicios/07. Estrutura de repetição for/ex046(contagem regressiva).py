'''Faça um programa que mostre na tela uma contagem regressiva para estouro de fogos
de artificio, indo de 10 até 0 com intervalo de 1 segundo.'''

print('>>>CONTAGEM REGRESSIVA<<<')

from time import sleep

for c in range(10, -1, -1):
    print(c)
    sleep(1)
print("BOOOMMMMM!!!")
