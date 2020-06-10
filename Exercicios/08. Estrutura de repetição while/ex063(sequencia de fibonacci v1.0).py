'''Escreva um programa que leia um numero n inteiro e mostre na tela os n primeiros
elementos de uma sequencia de Fibonacci'''

print("*-*-SEQUENCIA DE FIBONACCI-*-*")
print('~' * 35)
qtermos = int(input("Quantos termos deseja mostrar? "))
print('~' * 35)
t1 = 0
t2 = 1
print("{} ► {}".format(t1, t2), end=' ► ')
c = 3
while c <= qtermos:
    tfibo = t1 + t2
    print("{}".format(tfibo), end=' ► ')
    t1 = t2
    t2 = tfibo
    c += 1
print("FIM!")