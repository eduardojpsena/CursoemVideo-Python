'''Crie um programa que leia vários números inteiros. O programa só vai parar quando o
usuário digitar 999. No final mostre quantos números foram digitados e a soma entre eles'''

print(">>>TRATANDO VALORES V1<<<")

c = soma = 0
n = int(input("Digite um número (999 para parar o programa): "))
while n != 999:
    soma += n
    c += 1
    n = int(input("Digite um número (999 para parar o programa): "))
print("você digitou {} números a soma deles é {}.".format(c, soma))
