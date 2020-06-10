'''Faça um programa que calcule a soma entre todos os números impares que são multiplos
de 3 e se encontra no intervalo de 1 a 500'''

print("-=-=-TABUADA-=-=-")

soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        print(c)
        soma = soma + c
        cont = cont + 1
print("A soma de todos os {} valores solicitados é {}.".format(cont, soma))
