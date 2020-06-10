'''Crie um programa que simule o funcionamento de um caixa eletrônico. No início
pergunte ao usuário qual será o valor sacado(número inteiro) e o programa vai informar
quantas cédulas de cada valor serão entregues.
OBS: Considerar que o caixa possui cédulas de R$50, R$20, R$10 e R$1.'''

print("-=-=-SIMULADOR DE CAIXA ELETRÔNICO-=-=-")

print("~"*30)
print("{:^30}".format("BANCO SENA"))
print("~"*30)

valor = int(input("Qual valor deseja sacar? R$ "))
céd = 50
totalcéd = 0
while True:
    if valor >= céd:
        valor -= céd
        totalcéd += 1
    else:
        if totalcéd > 0:
            print(f"Total de {totalcéd} cédulas de R$ {céd}.")
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1
        totalcéd = 0
        if valor == 0:
            break
print("~"*30)
print("PROGRAMA FINALIZADO!!")
