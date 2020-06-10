'''Ler um número e mostrar seu dobro, triplo e raiz quadrada.'''

print(">>>DOBRO, TRIPLO E RAIZ QUADRADA<<<")

n = int(input("Digite um número: "))
print("→→→ O dobro de {} é {};".format(n, n*2))
print("→→→ O triplo de {} é {}; \n→→→ A raiz quadrada de {} é {:.2f}.".format(n, n*3, n, n**(1/2)))
