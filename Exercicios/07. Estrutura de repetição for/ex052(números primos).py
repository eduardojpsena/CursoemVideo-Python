'''Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.'''

print(">>>NÚMEROS PRIMOS<<<")

n = int(input("Digite um número: "))
total = 0
for c in range(1, n+1):
    if n % c == 0:
        print("\033[33m", end=" ")
        total = total + 1
    else:
        print("\033[31m", end=" ")
    print("{}".format(c), end=" ")
if total == 2:
    print("\n\033[mO número {} é divisivel por 2 números, portanto é PRIM0.".format(n))
else:
    print("\n\033[mO número {} é divisivel por {} números, portanto não é PRIMO".format(n, total))
