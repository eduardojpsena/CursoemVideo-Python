'''Escreva um programa que compare dois numeros inteiros e informe qual dos dois é maior.'''

print("\033[0;33m=-=-=Maior e menor valor=-=-=\033[m")

n1 = int(input("Digite um número inteiro: "))
n2 = int(input("Digite outro número inteiro: "))

if n1 > n2:
    print("{} é maior que {}.".format(n1, n2))
elif n2 > n1:
    print("{} é maior que {}.".format(n2, n1))
else:
    print("Os números {} e {} são iguais.".format(n1, n2))
