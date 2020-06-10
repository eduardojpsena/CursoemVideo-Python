'''Crie um programa que leia a velocidade de um carro, se ultrapassar 80km/h mostre
uma mensagem dizendo que foi multado, valor da multa 7 reais para cada km acima.'''

print(">>>RADAR ELETRÓNICO<<<")

velocidade = float(input("Qual é a velocidade atual do carro? "))
if velocidade <= 80:
    print("Tenha um bom dia, dirija com segurança!")
else:
    multa = (velocidade - 80) * 7
    print("Você ultrapassou a velocidade máxima permitida, será multado em R$ {:.2f} reais!".format(multa))
