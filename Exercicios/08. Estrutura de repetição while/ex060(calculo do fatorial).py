'''Faça um programa que leia um número qualquer e mostre seu fatorial'''

print("--==CALCULO DO FATORIAL==--")

n = int(input("Digite um número para calcular seu fatorial: "))
c = n
f = 1
print("•••Resultado fo fatorial de {}•••".format(n))

while c > 0:
    print(" {}".format(c), end=' ')
    print("x" if c > 1 else "=", end=' ')
    f *= c
    c -= 1
print(f)