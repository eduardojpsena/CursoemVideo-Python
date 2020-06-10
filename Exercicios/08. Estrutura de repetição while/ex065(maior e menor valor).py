'''Crie um programa que leia vários números inteiros. No final mostre a média de todos
os valores e qual foi o maior e menor valor. O programa deve perguntar ao usuário se
ele deseja continuar'''

print(">>>MAIOR E MENOR VALOR<<<")

soma = c = maior = menor = 0
situation = 'S'
while situation not in 'N':
    n = int(input("Digite um número: "))
    soma += n
    c += 1
    if c == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    situation = str(input("Deseja continuar? [S/N]: ")).strip().upper()[0]
media = soma/c
print("O maior valor foi {} e o menor foi {}".format(maior, menor))
print("A média entre os {} números digitados é: {}".format(c, media))