'''Crie um programa que leia um número inteiro e informe se o mesmo é par ou impar.'''

print(">>>PAR OU IMPAR<<<")

n = float(input("Digite um número qualquer: "))
if n % 2 == 1:
    print('O número {} é impar!'.format(n))
else:
    print("O número {} é par!".format(n))
