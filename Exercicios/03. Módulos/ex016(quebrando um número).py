'''Crie um Script que leia um número Real e mostre na tela sua porção inteira e
fracionada.'''

print(">>>QUEBRANDO UM NÚMERO<<<")

from math import trunc

n = float(input("Digite um número qualquer: "))
print("O número digitado foi {}, a sua porção inteira é {} e a fracionada é {:.3f}.".format(n, trunc(n), n-trunc(n)))
