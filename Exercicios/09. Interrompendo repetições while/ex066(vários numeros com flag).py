'''Crie um programa que leia vários números inteiros. O programa só vai parar quando o
usuário digitar 999. No final mostre quantos números foram digitados e a soma entre eles'''

print("*-*VÁRIOS NÚMEROS COM FLAG*-*")

c = soma = 0
while True:
    n = int(input("Digite um número [999 para encerrar]:"))
    if n == 999:
        break
    c += 1
    soma += n
print(f"A soma entre os {c} números digitados foi {soma}.")
