'''Faça um programa que programa que leia um número de 0 a 9999 e mostre na tela cada
um dos digitos separados.'''

print(">>>ANALISADOR DE TEXTO<<<")

num = int(input("Digite um número entre 0 e 9999: "))
u = num % 10
d = (num // 10) % 10
c = (num // 100) % 10
m = (num // 1000) % 10
print("Análisando o número", num)
print("Unidade:", u)
print("Dezenas:", d)
print("Centenas:", c)
print("Milhar:", m)
